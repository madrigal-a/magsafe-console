import pcbnew, sys
b=pcbnew.LoadBoard(sys.argv[1])
vias=[t for t in b.GetTracks() if t.GetClass()=='PCB_VIA']; rm=[]
for i,a in enumerate(vias):
    for c in vias[i+1:]:
        if a in rm or c in rm or a.GetNetCode()!=c.GetNetCode(): continue
        pa,pc=a.GetPosition(),c.GetPosition()
        if 0 < ((pa.x-pc.x)**2+(pa.y-pc.y)**2)**0.5 < 0.55e6:
            layers=set()
            for t in b.GetTracks():
                if t.GetClass()!='PCB_VIA' and t.GetNetCode()==c.GetNetCode() and (t.GetStart()==pc or t.GetEnd()==pc): layers.add((t.GetLayer(),t.GetWidth()))
            for L,w in layers:
                s=pcbnew.PCB_TRACK(b); s.SetStart(pc); s.SetEnd(pa); s.SetLayer(L); s.SetWidth(w); s.SetNet(c.GetNet()); b.Add(s)
            rm.append(c); print("vía unida en",pc.x/1e6,pc.y/1e6)
pcbnew.SaveBoard(sys.argv[1],b)
b=pcbnew.LoadBoard(sys.argv[1])
for t in list(b.GetTracks()):
    if t.GetClass()=='PCB_VIA' and any(t.GetPosition()==c.GetPosition() for c in rm): b.Remove(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); pcbnew.SaveBoard(sys.argv[1],b)
