gcode = 'G1 F1200 X-8.914 Y-9.843 E3.36222'
b=[[],[],[]]
c=""
d="9"
for a in gcode: 
    if d in ('0','1','2'):
        if a in ('-','0','1','2','3','4','5','6','7','8','9',' ','.'):
            c=c+a
        else:  
            e=int(d)
            b[int(d)]=c
            c="" 
            d="9"            
    if a=="X": d="0"     
    if a=="Y": d="1"   
    if a=="F": d="2"
print(b)
