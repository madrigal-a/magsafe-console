#!/bin/bash
cd /home/claude/route
PRESTITCH=$(cat prestitch.txt) python3 router.py magsafe-console.kicad_pcb routed.kicad_pcb > full.log 2>&1
tail -3 full.log
python3 - <<'PY'
import pcbnew
b=pcbnew.LoadBoard('routed.kicad_pcb')
zs=list(b.Zones())
if not any(z.GetLayer()==pcbnew.In2_Cu for z in zs):
    z=[z for z in zs if z.GetLayer()==pcbnew.F_Cu][0].Duplicate(); z.SetLayer(pcbnew.In2_Cu); b.Add(z)
for z in b.Zones(): z.SetIslandRemovalMode(pcbnew.ISLAND_REMOVAL_MODE_ALWAYS)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); pcbnew.SaveBoard('routed.kicad_pcb',b)
PY
python3 finalize.py routed.kicad_pcb | tail -9
for i in 1 2; do
  P=$(python3 islands.py routed.kicad_pcb | grep STITCHPT= | cut -d= -f2)
  [ -z "$P" ] && break
  RR=12 STITCHPT=$P python3 router.py routed.kicad_pcb routed.kicad_pcb | grep -i "vía de\|lugar"
done
python3 - <<'PY'
import pcbnew
b=pcbnew.LoadBoard('routed.kicad_pcb'); seen=set(); n=0
for t in list(b.GetTracks()):
    if t.GetClass()=='PCB_VIA': k=('v',t.GetPosition().x,t.GetPosition().y)
    else:
        a=(t.GetStart().x,t.GetStart().y); e=(t.GetEnd().x,t.GetEnd().y); k=('t',t.GetLayer(),min(a,e),max(a,e))
    if k in seen: b.Remove(t); n+=1
    else: seen.add(k)
print("duplicados quitados",n)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); pcbnew.SaveBoard('routed.kicad_pcb',b)
PY
python3 finalize.py routed.kicad_pcb | tail -9
python3 islands.py routed.kicad_pcb
