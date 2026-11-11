import json, re, subprocess, os, sys, pcbnew, collections
B = sys.argv[1]
def drc():
    subprocess.run(["kicad-cli","pcb","drc",B,"-o","drc.json","--format","json","--severity-all","--all-track-errors"],capture_output=True)
    return json.load(open("drc.json"))
for it in range(6):
    d = drc()
    pads = []
    for u in d["unconnected_items"]:
        for i in u["items"]:
            m = re.match(r"Pad (\S+) \[GND\] of (\S+) on", i["description"])
            if m: pads.append(m.group(2) + "." + m.group(1))
    starved = []
    for v in d["violations"]:
        if v["type"] == "starved_thermal":
            for i in v["items"]:
                m = re.match(r"Pad (\S+) \[GND\] of (\S+) on", i["description"])
                if m: starved.append((m.group(2), m.group(1)))
    print("pasada", it, "sin conectar:", len(d["unconnected_items"]), "pads:", sorted(set(pads)), "starved:", len(starved), flush=True)
    if not pads and not starved: break
    if pads:
        env = dict(os.environ, STITCH=",".join(sorted(set(pads))))
        r = subprocess.run(["python3","router.py",B,B],env=env,capture_output=True,text=True); print(r.stdout[-300:], r.stderr[-300:])
    if starved:
        b = pcbnew.LoadBoard(B)
        for ref, num in starved:
            for p in b.FindFootprintByReference(ref).Pads():
                if p.GetNumber() == num and p.GetNetname() == "GND": p.SetLocalZoneConnection(pcbnew.ZONE_CONNECTION_FULL)
        pcbnew.ZONE_FILLER(b).Fill(b.Zones()); pcbnew.SaveBoard(B, b)
d = drc()
c = collections.Counter((v["type"], v["severity"]) for v in d["violations"])
for k, v in c.most_common(): print(v, k)
print("sin conectar:", len(d["unconnected_items"]))
for u in d["unconnected_items"]: print("  ", " | ".join(i["description"][:70] for i in u["items"]))
