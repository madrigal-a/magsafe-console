import pcbnew, sys
from shapely.geometry import Polygon, Point
b=pcbnew.LoadBoard(sys.argv[1]); mm=lambda v:v/1e6
th=[]
for t in b.GetTracks():
    if t.GetClass()=='PCB_VIA' and t.GetNetname()=='GND': th.append(Point(mm(t.GetPosition().x),mm(t.GetPosition().y)))
smd=[]
for f in b.GetFootprints():
    for p in f.Pads():
        if p.GetNetname()!='GND': continue
        pt=Point(mm(p.GetPosition().x),mm(p.GetPosition().y))
        if p.GetAttribute()==pcbnew.PAD_ATTRIB_PTH: th.append(pt)
        else:
            bb=p.GetBoundingBox(); from shapely.geometry import box
            smd.append((f.GetReference()+'.'+p.GetNumber(), p.GetLayer(), box(mm(bb.GetX()),mm(bb.GetY()),mm(bb.GetRight()),mm(bb.GetBottom()))))
res=[]; pts=[]
for z in b.Zones():
    L=z.GetLayer(); ps=z.GetFilledPolysList(L)
    for i in range(ps.OutlineCount()):
        o=ps.Outline(i); ext=[(mm(o.CPoint(j).x),mm(o.CPoint(j).y)) for j in range(o.PointCount())]
        holes=[]
        for h in range(ps.HoleCount(i)):
            ho=ps.Hole(i,h); holes.append([(mm(ho.CPoint(j).x),mm(ho.CPoint(j).y)) for j in range(ho.PointCount())])
        pg=Polygon(ext,holes).buffer(0.02)
        if any(pg.contains(t) for t in th): continue
        pads=[n for n,l,pt in smd if l==L and pg.intersects(pt)]
        print(b.GetLayerName(L),"isla sin vía, área",round(pg.area,1),"pads",pads, [round(v,1) for v in pg.bounds])
        res+=pads[:2]
        r=Polygon(ext,holes).representative_point(); pts.append(f"{ {pcbnew.F_Cu:0,pcbnew.In2_Cu:1,pcbnew.B_Cu:2}.get(L,3)}:{r.x:.2f}:{r.y:.2f}")
rp=None
print("STITCH="+",".join(res))
print("STITCHPT="+",".join(pts))
