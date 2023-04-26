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


def gcode_exec(strg):
    global k
    for i in range(0,len(b),2): 
        if b[i]=="X":
            #r=float(b[i+1])
            k=5000
 
while True: 
    #led.value(not led.value())
    if k>0:
        k -=1        
        a +=1
        if a>8:
            a=1    
        if a==1:
            led.value(1) 
            led1.value(0) 
            led2.value(0) 
            led3.value(0) import usocket as socket
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


def gcode_exec(strg):
    global k
    for i in range(0,len(b),2): 
        if b[i]=="X":
            #r=float(b[i+1])
            k=5000
    if k==0:
        conn.send("ok\n")
while True: 
    #led.value(not led.value())
    if len(b)>0:
        if k==0:
            gcode_exec(b[0])
            b.remove(b[0])
    while k>0:
        k -=1  
        if k==0:                        
            conn.send("ok\n")
            break            
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
            conn.send("<Idle|MPos:0.000,0.000,0.000|FS:0,0>\r")
        else:      
            print("\r")        
            print(request)
            d=9
            c=""
            n=0
            for a1 in request:            
                if a1 in ('.','0','1','2','3','4','5','6','7','8','9',"-"):
                    m=0
                else:
                    m=1 
                    if a1=="\n":
                        b.append(c)
                        if c=="$$":
                            conn.send("ok\n")
                        #gcode_exec(b)                       
                        u=1
                        c=""                        
                        t=m                         
                        print(b)                        
                if t==m:
                    if not a1=="\n":                    
                        c +=a1
                else:                                     
                    b.append(c)
                    c=a1
                t=m                                            
                 
    except OSError as e:
        time.sleep_us(200)                 
      
# Clean up the connection.
conn.close()
print("closed. ") 
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
            conn.send("<Idle|MPos:0.000,0.000,0.000|FS:0,0>\r")
        else:      
            print("\r")        
            print(request)
            b=[]
            d=9
            c=""
            n=0
            for a1 in request:            
                if a1 in ('.','0','1','2','3','4','5','6','7','8','9',"-"):
                    m=0
                else:
                    m=1 
                    if a1=="\n":
                        b.append(c)
                        gcode_exec(b) 
                        b=[]
                        c=""                        
                        t=m                        
                if t==m:
                    if not a1=="\n":                    
                        c +=a1
                else:                                     
                    b.append(c)
                    c=a1
                t=m                    
                                    
            conn.send("ok\n") 
    except OSError as e:
        time.sleep_us(200)                 
      
# Clean up the connection.
conn.close()
print("closed. ") 
