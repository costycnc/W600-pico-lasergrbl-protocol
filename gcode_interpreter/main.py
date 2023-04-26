import usocket as socket
import time
from machine import Pin


led = Pin(Pin.PB_12, Pin.OUT, Pin.PULL_FLOATING)
led1 = Pin(Pin.PB_11, Pin.OUT, Pin.PULL_FLOATING)
led2 = Pin(Pin.PB_10, Pin.OUT, Pin.PULL_FLOATING)
led3 = Pin(Pin.PB_09, Pin.OUT, Pin.PULL_FLOATING)
led4 = Pin(Pin.PB_18, Pin.OUT, Pin.PULL_FLOATING)
s = socket.socket()
s.bind(('', 23))
s.listen(5)
conn, addr = s.accept()
conn.setblocking(False)
a=0
b=[]
c=""
d=0
k=1
l=0
m=0
n=0
t=0
u=0
v=[]
x=0
y=0


def extract(a4):
    vrt=""
    for a5 in a4:    
        if  a5 in('.','0','1','2','3','4','5','6','7','8','9',"-"):
            vrt +=a5
        else:
            break
    return vrt    

def gcode_exec(strg):
    global k,u,x,y
    if "X" in strg:
        nn=strg.split("X")
        k=int(float(extract(nn[1])))
        x=k
        k=k*100
    if "Y" in strg:
        nn=strg.split("Y")
        y=int(float(extract(nn[1])))        
    else:
        u=0    
        

while True: 
    #led.value(not led.value())
    if u==0:
        u=1
        if v:
            print("gcode")
            gcode_exec(v.pop(0))
            conn.send("ok\n")
        else:
            u=0
    if k>0:
        time.sleep_us(200)
        k -=1
        if k==0:
            u=0        
        a +=1
        if a>8:
            a=1    
        if a==1:
            led.value(1) 
            led1.value(0) 
            led2.value(0) 
            led3.value(0) 
        if a==2:
            led.value(1) 
            led1.value(1) 
            led2.value(0) 
            led3.value(0) 
        if a==3:
            led.value(0) 
            led1.value(1) 
            led2.value(0) 
            led3.value(0) 
        if a==4:
            led.value(0) 
            led1.value(1) 
            led2.value(1) 
            led3.value(0)        
        if a==5:
            led.value(0) 
            led1.value(0) 
            led2.value(1) 
            led3.value(0)  
        if a==6:
            led.value(0) 
            led1.value(0) 
            led2.value(1) 
            led3.value(1)  
        if a==7:
            led.value(0) 
            led1.value(0) 
            led2.value(0) 
            led3.value(1)  
        if a==8:
            led.value(1) 
            led1.value(0) 
            led2.value(0) 
            led3.value(1)    
    try:       
        request = conn.recv(200).decode()                                  
        if "?" in request:   
            conn.send("<Idle|MPos:"+str(x)+","+str(y)+",0.000|FS:0,0>\r")
        elif "$$" in request:
            conn.send("ok\n")
        else: 
            b=request.split("\n")
            for ax in b:            
                #gcode_exec(ax)
                v.append(ax)

                
    except OSError as e:
        pass                 
      
# Clean up the connection.
conn.close()
print("closed. ") 