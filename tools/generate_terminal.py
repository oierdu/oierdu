from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json
R=Path(__file__).resolve().parent.parent
P=R; A=P/'assets'; A.mkdir(exist_ok=True)
O=R/'work'; O.mkdir(exist_ok=True); (O/'animation-proof').mkdir(exist_ok=True)
mono=ImageFont.truetype('C:/Windows/Fonts/consola.ttf',18)
def terminal(theme,mobile=False):
    w,h=(360,218) if mobile else (680,208)
    bg,top,ink,muted,line=('#171c23','#202731','#e6edf3','#9ba8b8','#343e4b') if theme=='dark' else ('#faf9f5','#eeede7','#252b34','#66717f','#deded4')
    font=ImageFont.truetype('C:/Windows/Fonts/consola.ttf',15 if mobile else 18)
    title=ImageFont.truetype('C:/Windows/Fonts/consola.ttf',12)
    labels=['~/oierdu $ ./portfolio','> Loading projects...','> Software engineering','> Backend & databases','> Applied AI','> Building useful things']
    starts=[0.3,1.6,3.2,5.1,7.0,8.5]
    def draw(t,still=False):
        im=Image.new('RGB',(w,h),bg);d=ImageDraw.Draw(im)
        d.rounded_rectangle((0,0,w-1,h-1),radius=12,fill=bg,outline=line,width=1)
        d.rounded_rectangle((1,1,w-2,35),radius=11,fill=top);d.rectangle((1,23,w-2,35),fill=top)
        for x,c in [(18,'#e89c94'),(35,'#dbbd7a'),(52,'#93bea1')]:d.ellipse((x,14,x+7,21),fill=c)
        d.text((w-132,11),'portfolio / oierdu',font=title,fill=muted)
        active=0;shown=[]
        for i,label in enumerate(labels):
            n=len(label) if still else min(len(label),max(0,round((t-starts[i])/0.05)))
            if not still and t>=13.5:n=max(0,n-int((t-13.5)*22)-(len(labels)-i-1)*0)
            shown.append(label[:n])
            if n:active=i
            color=('#a7d7b5' if theme=='dark' else '#276747') if i in [0,5] else (ink if i<4 else muted)
            d.text((20,48+i*25),label[:n],font=font,fill=color)
        if not still and int(t*2)%2==0:
            x=20+d.textlength(shown[active],font=font);y=48+active*25
            d.rectangle((x+2,y+2,x+10,y+18),fill='#a7d7b5' if theme=='dark' else '#276747')
        return im
    frames=[draw(i/20) for i in range(340)]
    name=f'terminal-{theme}'+('-mobile' if mobile else '')
    frames[0].save(A/(name+'.gif'),save_all=True,append_images=frames[1:],duration=50,loop=0,optimize=True,disposal=1)
    draw(11,True).save(A/(name+'-still.png'),optimize=True)
    for seconds in [20,40]:draw(seconds%17).save(O/'animation-proof'/f'{name}-{seconds}s.png')
    gif=Image.open(A/(name+'.gif'))
    return {'file':name+'.gif','bytes':(A/(name+'.gif')).stat().st_size,'frames':gif.n_frames,'duration_ms':sum((gif.seek(i) or gif.info['duration']) for i in range(gif.n_frames)),'loop':gif.info.get('loop')}
qa=[terminal(t,m) for t in ['dark','light'] for m in [False,True]]
(O/'animation-proof/encoding.json').write_text(json.dumps(qa,indent=2),encoding='utf-8')
