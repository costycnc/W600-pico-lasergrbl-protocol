b=["0","0","0"]
request="G01 X100.123 Y200\n"
d=9
c=""
for a in request:            
    if d in (0,1,2):
        if str(a) in ('.','-','0','1','2','3','4','5','6','7','8','9',' '):
            c=c+str(a)
        else:                                           
            b[d]=c                           
            c="" 
            d="9"            
    if str(a)=="X": d=0   
    if str(a)=="Y": d=1   
    if str(a)=="G": d=2
print(b[0])   
print(b[1])            
print(b[2])   
