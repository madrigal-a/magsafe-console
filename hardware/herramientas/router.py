#!/usr/bin/env python3
"""Trazador de rejilla para magsafe-console. Uso: router.py entrada.kicad_pcb salida.kicad_pcb"""
import sys, heapq, time, os
import numpy as np
import pcbnew
import shapely
from shapely.geometry import Polygon, Point, LineString, box
from shapely.ops import unary_union

SRC, DST = sys.argv[1], sys.argv[2]
G = 0.1                       # paso de rejilla, mm
X0, Y0, X1, Y1 = 100.0, 50.0, 164.0, 148.0
W = int(round((X1 - X0) / G)) + 1
H = int(round((Y1 - Y0) / G)) + 1
CLR = 0.15
MARGIN = 0.02
W_SIG, W_PWR, W_NECK = 0.2, 0.4, 0.2
VIA_D, VIA_DRILL = 0.6, 0.3
EDGE = 0.3
# inflados: 0 = pista fina, 1 = pista ancha, 2 = vía
RAD = [W_SIG / 2 + CLR + MARGIN, W_PWR / 2 + CLR + MARGIN, VIA_D / 2 + CLR + MARGIN]
LAYERS = [pcbnew.F_Cu, pcbnew.In2_Cu, pcbnew.B_Cu, pcbnew.In1_Cu]   # índices 0..2 se trazan; 3 = plano
NL = 3
POWER = {"/VBUS", "/VBAT", "/VSYS", "/+3V3", "/3V3_REG", "/SPK_P", "/SPK_N"}

b = pcbnew.LoadBoard(SRC)
mm = lambda v: v / 1e6

def poly_from_set(ps):
    out = []
    for i in range(ps.OutlineCount()):
        o = ps.Outline(i)
        pts = [(mm(o.CPoint(j).x), mm(o.CPoint(j).y)) for j in range(o.PointCount())]
        if len(pts) >= 3:
            out.append(Polygon(pts).buffer(0))
    return unary_union(out) if out else None

cnt = np.zeros((3, 4, W, H), dtype=np.int16)
obst = {}     # net -> lista de (kind, capa_idx, [(x0,y0,mask) por radio])

def raster(geom, r):
    g = geom.buffer(r)
    minx, miny, maxx, maxy = g.bounds
    ix0 = max(0, int(np.floor((minx - X0) / G))); ix1 = min(W - 1, int(np.ceil((maxx - X0) / G)))
    iy0 = max(0, int(np.floor((miny - Y0) / G))); iy1 = min(H - 1, int(np.ceil((maxy - Y0) / G)))
    if ix1 < ix0 or iy1 < iy0:
        return None
    xs = X0 + G * np.arange(ix0, ix1 + 1); ys = Y0 + G * np.arange(iy0, iy1 + 1)
    XX, YY = np.meshgrid(xs, ys, indexing="ij")
    m = shapely.contains_xy(g, XX, YY)
    return (ix0, iy0, m)

def add_obst(net, kind, li, geom):
    rs = [raster(geom, r) for r in RAD]
    obst.setdefault(net, []).append((kind, li, rs))
    apply(rs, li, +1)

def apply(rs, li, sign, ks=(0, 1, 2)):
    for k in ks:
        if rs[k] is None: continue
        x0, y0, m = rs[k]
        cnt[k, li, x0:x0 + m.shape[0], y0:y0 + m.shape[1]] += sign * m.astype(np.int16)

# --- contorno y zonas prohibidas
outl = pcbnew.SHAPE_POLY_SET(); b.GetBoardPolygonOutlines(outl)
board_poly = poly_from_set(outl)
world = box(X0 - 5, Y0 - 5, X1 + 5, Y1 + 5)
edge_block = world.difference(board_poly.buffer(-EDGE))
for li in range(4):
    add_obst(None, "fix", li, edge_block)
for f in b.GetFootprints():
    for z in f.Zones():
        if z.GetIsRuleArea():
            zp = poly_from_set(z.Outline())
            for li in range(4):
                add_obst(None, "fix", li, zp)

# --- cuerpos de conectores: sin pistas ni vías en la cara de atrás
for bx in (box(127.1, 141.25, 136.9, 149.0), box(150.05, 122.95, 164.5, 137.05)):
    add_obst(None, "fix", 2, bx)
# --- pads
padinfo = {}   # net -> lista de (ref.num, capas_idx, geom)
for f in b.GetFootprints():
    for p in f.Pads():
        net = p.GetNetname() or None
        attr = p.GetAttribute()
        if attr == pcbnew.PAD_ATTRIB_NPTH:
            d = mm(max(p.GetDrillSize().x, p.GetDrillSize().y))
            c = Point(mm(p.GetPosition().x), mm(p.GetPosition().y)).buffer(d / 2 + 0.12)
            for li in range(4): add_obst(None, "fix", li, c)
            continue
        lis = [i for i, L in enumerate(LAYERS) if p.IsOnLayer(L)]
        for li in lis:
            ps = pcbnew.SHAPE_POLY_SET()
            p.TransformShapeToPolygon(ps, LAYERS[li], 0, 2000, pcbnew.ERROR_OUTSIDE)
            g = poly_from_set(ps)
            if g is None: continue
            add_obst(net, "pad", li, g)
            if net and li < NL:
                padinfo.setdefault(net, []).append((f.GetReference() + "." + p.GetNumber(), li, g))
    for gi in f.GraphicalItems():
        for li, L in enumerate(LAYERS):
            if gi.GetLayer() == L:
                ps = pcbnew.SHAPE_POLY_SET()
                gi.TransformShapeToPolygon(ps, L, 0, 2000, pcbnew.ERROR_OUTSIDE)
                g = poly_from_set(ps)
                if g is not None: add_obst(None, "fix", li, g)

# pistas y vías ya existentes
for t in b.GetTracks():
    net = t.GetNetname() or None
    if t.GetClass() == "PCB_VIA":
        c = Point(mm(t.GetPosition().x), mm(t.GetPosition().y)).buffer(mm(t.GetWidth(pcbnew.F_Cu)) / 2)
        for li in range(4): add_obst(net, "route", li, c)
    else:
        li = LAYERS.index(t.GetLayer())
        ls = LineString([(mm(t.GetStart().x), mm(t.GetStart().y)), (mm(t.GetEnd().x), mm(t.GetEnd().y))]).buffer(mm(t.GetWidth()) / 2)
        add_obst(net, "route", li, ls)

def cells_in(geom):
    r = raster(geom, 0.0)
    if r is None: return []
    x0, y0, m = r
    xs, ys = np.nonzero(m)
    return [(x0 + int(a), y0 + int(c)) for a, c in zip(xs, ys)]

DIRS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
DCOST = [10, 14, 10, 14, 10, 14, 10, 14]
VIA_COST = 250
TURN = 4
LAYER_MULT = [1.0, 1.0, 1.0]

def route_net(net, results, maxexp=2500000):
    """Devuelve lista de rutas [(li,x,y),...] o None."""
    power = net in POWER
    own = obst.get(net, [])
    for kind, li, rs in own:
        apply(rs, li, -1, ks=(0, 1))
        if kind == "route": apply(rs, li, -1, ks=(2,))
    try:
        nb = cnt[0, :NL] > 0
        wb = cnt[1, :NL] > 0
        if power:
            st = np.where(~wb, 1, np.where(~nb, 2, 0)).astype(np.uint8)
        else:
            st = np.where(~nb, 1, 0).astype(np.uint8)
        viaok = (cnt[2].sum(axis=0) == 0)
        if os.environ.get("DEBUGST"):
            cx,cy=[float(v) for v in os.environ["DEBUGST"].split(":")]; ix=int(round((cx-X0)/G)); iy=int(round((cy-Y0)/G))
            for l in range(NL):
                print("capa",l)
                for y in range(iy-9,iy+10): print("".join(str(st[l][x,y]) for x in range(ix-12,ix+13)))
        stb = [st[l].tobytes() for l in range(NL)]
        viab = viaok.astype(np.uint8).tobytes()
        pads = padinfo[net]
        grp = {}
        for name, li, g in pads:
            cs = cells_in(g)
            if not cs:
                c = g.centroid
                cs = [(int(round((c.x - X0) / G)), int(round((c.y - Y0) / G)))]
            e = grp.setdefault(name, [name, [], (g.centroid.x, g.centroid.y)])
            e[1] += [(li, x, y) for x, y in cs]
        padcells = [tuple(v) for v in grp.values()]   # (nombre, [(capa,x,y)...], centro)
        # árbol: se parte del primer pad y se van uniendo los demás, el más cercano primero
        if net in pretree:
            tree = set(pretree[net]); treepts = [(X0 + x * G, Y0 + y * G) for (l, x, y) in list(pretree[net])[::5]]
            remaining = padcells[:]
        else:
            tree = set(padcells[0][1])
            treepts = [padcells[0][2]]
            remaining = padcells[1:]
        paths = []
        while remaining:
            # ¿algún pad ya tocado por el árbol?
            rem2 = []
            for pc in remaining:
                if any(c in tree for c in pc[1]):
                    tree.update(pc[1]); treepts.append(pc[2])
                else:
                    rem2.append(pc)
            remaining = rem2
            if not remaining: break
            remaining.sort(key=lambda pc: min((pc[2][0] - t[0]) ** 2 + (pc[2][1] - t[1]) ** 2 for t in treepts))
            pc = remaining.pop(0)
            path = astar(pc, tree, treepts, stb, viab, power, maxexp)
            if path is None:
                print("   fallo:", net, pc[0], flush=True)
                return None
            paths.append(path)
            tree.update(path)
            tree.update(pc[1])
            treepts.append(pc[2])
            step = max(1, len(path) // 6)
            for (l, x, y) in path[::step]:
                treepts.append((X0 + x * G, Y0 + y * G))
        return paths, st
    finally:
        for kind, li, rs in own:
            apply(rs, li, +1, ks=(0, 1))
            if kind == "route": apply(rs, li, +1, ks=(2,))

def astar(pc, tree, treepts, stb, viab, power, maxexp):
    name, scells, _ = pc
    tp = [((tx - X0) / G, (ty - Y0) / G) for tx, ty in treepts]
    if len(tp) > 10: tp = tp[::max(1, len(tp) // 10)]
    def h(x, y):
        best = 1e18
        for tx, ty in tp:
            dx = abs(x - tx); dy = abs(y - ty)
            d = 10 * max(dx, dy) + 4 * min(dx, dy)
            if d < best: best = d
        return int(best * 1.25)
    openq = []
    best = {}
    parent = {}
    for (sli, x, y) in scells:
        s = (((sli * W + x) * H + y) * 9) + 8
        best[s] = 0
        heapq.heappush(openq, (h(x, y), 0, s))
    exp = 0
    while openq:
        f, g, s = heapq.heappop(openq)
        if best.get(s, 1 << 60) < g: continue
        d = s % 9; r = s // 9
        y = r % H; r //= H
        x = r % W; l = r // W
        if (l, x, y) in tree:
            path = [(l, x, y)]
            while s in parent:
                s = parent[s]
                r = s // 9; yy = r % H; r //= H; xx = r % W; ll = r // W
                if path[-1] != (ll, xx, yy): path.append((ll, xx, yy))
            return path[::-1]
        exp += 1
        if exp > maxexp: return None
        sb = stb[l]
        for nd in range(8):
            if d != 8:
                turn = abs(nd - d); turn = min(turn, 8 - turn)
                if turn > 2: continue
            else:
                turn = 0
            dx, dy = DIRS[nd]
            nx = x + dx; ny = y + dy
            if nx < 0 or ny < 0 or nx >= W or ny >= H: continue
            v = sb[nx * H + ny]
            if v == 0:
                if (l, nx, ny) not in tree: continue
                v = 1
            if nd & 1:   # diagonal: no cortar esquinas
                if sb[nx * H + y] == 0 and sb[x * H + ny] == 0: continue
            c = DCOST[nd] * (3 if v == 2 else 1) * LAYER_MULT[l] + TURN * turn
            ng = g + int(c)
            ns = (((l * W + nx) * H + ny) * 9) + nd
            if ng < best.get(ns, 1 << 60):
                best[ns] = ng; parent[ns] = s
                heapq.heappush(openq, (ng + h(nx, ny), ng, ns))
        if viab[x * H + y]:
            for nl in range(NL):
                if nl == l: continue
                if stb[nl][x * H + y] == 0: continue
                ng = g + VIA_COST
                ns = (((nl * W + x) * H + y) * 9) + 8
                if ng < best.get(ns, 1 << 60):
                    best[ns] = ng; parent[ns] = s
                    heapq.heappush(openq, (ng + h(x, y), ng, ns))
    return None

def emit(net, paths, st, out):
    """Convierte rutas en segmentos y vías, y las registra como obstáculos."""
    power = net in POWER
    for path in paths:
        i = 0
        n = len(path)
        while i < n - 1:
            l, x, y = path[i]
            l2, x2, y2 = path[i + 1]
            if l2 != l:
                pt = (X0 + x * G, Y0 + y * G)
                out.append(("via", net, pt))
                c = Point(pt).buffer(VIA_D / 2)
                for li in range(4): add_obst(net, "route", li, c)
                i += 1
                continue
            # tramo recto en la misma capa con el mismo ancho
            def wid(a, c):
                if not power: return W_SIG
                return W_PWR if (st[l][a[1], a[2]] == 1 and st[l][c[1], c[2]] == 1) else W_NECK
            d = (x2 - x, y2 - y); w = wid(path[i], path[i + 1])
            j = i + 1
            while j < n - 1:
                a = path[j]; c = path[j + 1]
                if c[0] != l or (c[1] - a[1], c[2] - a[2]) != d or wid(a, c) != w: break
                j += 1
            p1 = (X0 + x * G, Y0 + y * G); p2 = (X0 + path[j][1] * G, Y0 + path[j][2] * G)
            out.append(("seg", net, l, p1, p2, w))
            add_obst(net, "route", l, LineString([p1, p2]).buffer(w / 2))
            i = j

def cells_of(wps):
    out = []
    for (l, x, y) in wps:
        c = (l, int(round((x - X0) / G)), int(round((y - Y0) / G)))
        if not out: out.append(c); continue
        p = out[-1]
        if p[0] != l:
            assert (p[1], p[2]) == (c[1], c[2]); out.append(c); continue
        dx = c[1] - p[1]; dy = c[2] - p[2]
        n = max(abs(dx), abs(dy))
        assert dx == 0 or dy == 0 or abs(dx) == abs(dy), (wps, c)
        sx = (dx > 0) - (dx < 0); sy = (dy > 0) - (dy < 0)
        for k in range(1, n + 1): out.append((l, p[1] + sx * k, p[2] + sy * k))
    return out

# Salida del USB-C trazada a mano (los pads de D+ y D- van intercalados)
PRE = {}
pretree = {}

def order_key(net):
    pri = {"/USB_DP": 0, "/USB_DM": 0, "/CC1": 1, "/CC2": 1, "/VBUS": 2, "/VBAT": 2, "/VSYS": 2, "/3V3_REG": 2,
           "/+3V3": 3, "/SPK_P": 3, "/SPK_N": 3, "/EN": 4}
    ps = padinfo[net]
    xs = [g.centroid.x for _, _, g in ps]; ys = [g.centroid.y for _, _, g in ps]
    span = (max(xs) - min(xs)) + (max(ys) - min(ys))
    return (pri.get(net, 5), span)

nets = [n for n in padinfo if n != "GND" and not n.startswith("unconnected") and len(set(p[0] for p in padinfo[n])) >= 2]
nets.sort(key=order_key)
ONLY = sys.argv[3].split(",") if len(sys.argv) > 3 else None
if ONLY: nets = [n for n in nets if n in ONLY]
print(len(nets), "redes", flush=True)
out = []

import os, collections
def stitch(padname, out):
    cand = [p for p in padinfo.get("GND", []) if p[0] == padname]
    if not cand: print("  sin pad", padname); return False
    own = obst.get("GND", [])
    for kind, li, rs in own:
        apply(rs, li, -1, ks=(0, 1))
        if kind == "route": apply(rs, li, -1, ks=(2,))
    try:
        viaok = (cnt[2].sum(axis=0) == 0)
        for name, li, g in cand:
            free = cnt[0, li] == 0
            start = cells_in(g)
            seen = {c: None for c in start}
            dq = collections.deque(start); found = None
            while dq:
                c = dq.popleft()
                if viaok[c[0], c[1]] and free[c[0], c[1]]:
                    found = c; break
                for dx, dy in DIRS:
                    n = (c[0] + dx, c[1] + dy)
                    if dx and dy and not (free[c[0] + dx, c[1]] and free[c[0], c[1] + dy]): continue
                    if n in seen or not (0 <= n[0] < W and 0 <= n[1] < H): continue
                    if not free[n[0], n[1]] and n not in start: continue
                    if abs(n[0] - start[0][0]) > 45 or abs(n[1] - start[0][1]) > 45: continue
                    seen[n] = c; dq.append(n)
            if found is None: continue
            path = [found]
            while seen[path[-1]] is not None: path.append(seen[path[-1]])
            path = [(li, x, y) for x, y in path[::-1]]
            path.append(((li + 1) % NL, found[0], found[1]))   # fuerza la vía
            stf = np.zeros((NL, W, H), dtype=np.uint8)
            return path
    finally:
        for kind, li, rs in own:
            apply(rs, li, +1, ks=(0, 1))
            if kind == "route": apply(rs, li, +1, ks=(2,))
    print("  sin lugar para vía:", padname); return None

STITCH = os.environ.get("STITCH")
if STITCH:
    out = []
    for pn in STITCH.split(","):
        p = stitch(pn, out)
        if p: emit("GND", [p], np.zeros((NL, W, H), dtype=np.uint8), out)
    nets = ["GND"]; order = []
SPT = os.environ.get("STITCHPT"); RR = int(os.environ.get("RR", "30"))
if SPT:
    out = []
    for item in SPT.split(","):
        li, x, y = item.split(":"); li = int(li); cx = int(round((float(x) - X0) / G)); cy = int(round((float(y) - Y0) / G))
        own = obst.get("GND", [])
        for kind, l2, rs in own:
            apply(rs, l2, -1, ks=(0, 1))
            if kind == "route": apply(rs, l2, -1, ks=(2,))
        viaok = (cnt[2].sum(axis=0) == 0) & (cnt[0, li] == 0)
        for kind, l2, rs in own:
            apply(rs, l2, +1, ks=(0, 1))
            if kind == "route": apply(rs, l2, +1, ks=(2,))
        xs, ys = np.nonzero(viaok[max(0, cx - RR):cx + RR + 1, max(0, cy - RR):cy + RR + 1])
        if len(xs) == 0: print("  sin lugar", item); continue
        xs = xs + max(0, cx - RR); ys = ys + max(0, cy - RR)
        k = np.argmin((xs - cx) ** 2 + (ys - cy) ** 2)
        pt = (X0 + xs[k] * G, Y0 + ys[k] * G)
        out.append(("via", "GND", pt))
        for l2 in range(4): add_obst("GND", "route", l2, Point(pt).buffer(VIA_D / 2))
        print("  vía de tierra en", pt)
    nets = ["GND"]; order = []
pre_out = []
PS = os.environ.get("PRESTITCH")
if PS and not (STITCH or SPT):
    for pn in PS.split(","):
        p = stitch(pn, pre_out)
        if p: emit("GND", [p], np.zeros((NL, W, H), dtype=np.uint8), pre_out)
    nets.append("GND")
import copy
base_cnt = cnt.copy(); base_obst = {k: list(v) for k, v in obst.items()}
order = [n for n in nets if n != 'GND']
for attempt in range(0 if (STITCH or SPT) else 12):
    cnt[:] = base_cnt; obst.clear(); obst.update({k: list(v) for k, v in base_obst.items()})
    out = []; failed = None
    t0 = time.time()
    pretree.clear()
    for pn, pths in PRE.items():
        if pn not in nets: continue
        cps = [cells_of(w) for w in pths]
        stfake = np.zeros((NL, W, H), dtype=np.uint8)
        emit(pn, cps, stfake, out)
        pretree[pn] = set(c for cp in cps for c in cp)
    for net in order:
        res = route_net(net, out)
        if res is None:
            failed = net; break
        emit(net, res[0], res[1], out)
    print("intento", attempt, "fallo en" if failed else "completo", failed or "", round(time.time() - t0), "s", flush=True)
    if not failed: break
    order.remove(failed); order.insert(0, failed)
else:
    print("NO SE COMPLETÓ");

# escribir
out = pre_out + out
netmap = {n: b.FindNet(n) for n in nets}
def cell(p): return (int(round((p[0] - X0) / G)), int(round((p[1] - Y0) / G)))
ends = {}
for it in out:
    if it[0] == "via":
        for l in range(NL): ends.setdefault((it[1], l), set()).add(cell(it[2]))
    else:
        ends.setdefault((it[1], it[2]), set()).update([cell(it[3]), cell(it[4])])
out2 = []; seenvia = set()
for it in out:
    if it[0] == "via":
        k = (it[1], cell(it[2]))
        if k in seenvia: continue
        seenvia.add(k); out2.append(it); continue
    _, net, l, p1, p2, w = it
    a = cell(p1); c = cell(p2); n = max(abs(c[0] - a[0]), abs(c[1] - a[1]))
    if n == 0: continue
    sx = (c[0] > a[0]) - (c[0] < a[0]); sy = (c[1] > a[1]) - (c[1] < a[1])
    last = a
    for k in range(1, n + 1):
        q = (a[0] + sx * k, a[1] + sy * k)
        if k == n or q in ends[(net, l)]:
            out2.append(("seg", net, l, (X0 + last[0] * G, Y0 + last[1] * G), (X0 + q[0] * G, Y0 + q[1] * G), w)); last = q
out = out2
nv = ns = 0
for it in out:
    if it[0] == "via":
        v = pcbnew.PCB_VIA(b)
        v.SetPosition(pcbnew.VECTOR2I(int(round(it[2][0] * 1e6)), int(round(it[2][1] * 1e6))))
        v.SetViaType(pcbnew.VIATYPE_THROUGH)
        v.SetWidth(pcbnew.F_Cu, int(VIA_D * 1e6)) if v.SetWidth.__doc__ and "PCB_LAYER_ID" in v.SetWidth.__doc__ else v.SetWidth(int(VIA_D * 1e6))
        v.SetDrill(int(VIA_DRILL * 1e6))
        v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
        v.SetNet(netmap[it[1]]); b.Add(v); nv += 1
    else:
        _, net, l, p1, p2, w = it
        t = pcbnew.PCB_TRACK(b)
        t.SetStart(pcbnew.VECTOR2I(int(round(p1[0] * 1e6)), int(round(p1[1] * 1e6))))
        t.SetEnd(pcbnew.VECTOR2I(int(round(p2[0] * 1e6)), int(round(p2[1] * 1e6))))
        t.SetWidth(int(round(w * 1e6))); t.SetLayer(LAYERS[l]); t.SetNet(netmap[net]); b.Add(t); ns += 1
print("segmentos", ns, "vías", nv)
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
pcbnew.SaveBoard(DST, b)
