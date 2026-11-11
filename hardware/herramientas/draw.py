import sys, pcbnew
from PIL import Image, ImageDraw
src,out=sys.argv[1],sys.argv[2]
x0,y0,x1,y1=[float(v) for v in sys.argv[3:7]] if len(sys.argv)>6 else (99,49,165,149)
S=float(sys.argv[7]) if len(sys.argv)>7 else 12
only=sys.argv[8].split(',') if len(sys.argv)>8 else ['F','In2','B']
b=pcbnew.LoadBoard(src)
im=Image.new('RGB',(int((x1-x0)*S),int((y1-y0)*S)),'white'); d=ImageDraw.Draw(im,'RGBA')
P=lambda x,y:((x/1e6-x0)*S,(y/1e6-y0)*S)
col={pcbnew.F_Cu:(220,40,40,150),pcbnew.In2_Cu:(40,170,40,170),pcbnew.B_Cu:(40,70,220,150),pcbnew.In1_Cu:(200,160,0,150)}
nm={'F':pcbnew.F_Cu,'In2':pcbnew.In2_Cu,'B':pcbnew.B_Cu}
ls=[nm[o] for o in only]
o=pcbnew.SHAPE_POLY_SET(); b.GetBoardPolygonOutlines(o); ol=o.Outline(0)
d.line([P(ol.CPoint(i).x,ol.CPoint(i).y) for i in range(ol.PointCount())]+[P(ol.CPoint(0).x,ol.CPoint(0).y)],fill=(0,0,0,255),width=2)
for f in b.GetFootprints():
    for p in f.Pads():
        for L in ls:
            if p.IsOnLayer(L):
                ps=pcbnew.SHAPE_POLY_SET(); p.TransformShapeToPolygon(ps,L,0,5000,pcbnew.ERROR_INSIDE)
                if ps.OutlineCount():
                    q=ps.Outline(0); c=col[L] if p.GetNetname()!='GND' else (120,120,120,120)
                    d.polygon([P(q.CPoint(i).x,q.CPoint(i).y) for i in range(q.PointCount())],fill=c)
    if S>=10:
        pos=f.GetPosition(); d.text(P(pos.x,pos.y),f.GetReference(),fill=(0,0,0,255))
for t in b.GetTracks():
    if t.GetClass()=='PCB_VIA':
        x,y=P(t.GetPosition().x,t.GetPosition().y); r=0.3*S
        d.ellipse((x-r,y-r,x+r,y+r),fill=(0,0,0,200) if t.GetNetname()!='GND' else (120,120,120,220))
    elif t.GetLayer() in ls:
        d.line([P(t.GetStart().x,t.GetStart().y),P(t.GetEnd().x,t.GetEnd().y)],fill=col[t.GetLayer()],width=max(1,int(t.GetWidth()/1e6*S)))
im.save(out); print(im.size)
