# 25.02.2023
import usocket as socket
import time
import re
from machine import Timer
import _thread



s = socket.socket()
s.bind(('', 23))
s.listen(5)
conn, addr = s.accept()
conn.setblocking(False)

a=0
variable=[]
b=["0","0","0"]
c=""
d=8
valx=0
eee=0
f=0
cont=0
xvar=[]
xvar1=[]
xvar2=[]
xvar3=[]
test=0
test1=0
#timer1 = Timer(-1)
#timer1.init(period=500, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
timer3 = Timer(3)
timer3.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:prt())

def prt():
    global test1
    print(test1)
    

 
while True:
    if len(xvar)>0:
        if test==0:
            xvar1=xvar.pop(0)
            xvar2=xvar1.split("\n")
            test=1 # cand xvar2 contine risposta cu elementi
            if xvar2[0]=="\x18":test=0
            if xvar2[0]=="$$": test=0          
    if test==1:
        if len(xvar2)>0:
            xvar3=xvar2.pop(0) # test2 blocheaza bucla si asteapta pana timer proceseaza element
            test=2 # cand xvar3 contine un element din xvar2
        else:
            test=0  
    if test==2:
        test1=test1+1
        #print(xvar3) # intorcere din timer ... timer scrie test=5
        test=1 # cere alt element
        #conn.send("ok\r")
        
            
    try:
        request = conn.recv(200) 
               
        if request: 
            if "?" in request:                                                   
                conn.send("<Idle|MPos:"+b[0]+","+b[1]+",0.000|FS:0,0>\r")
            else:
                xvar.append(request.decode())        
        else:
            print('No data: connection closed by the client')
            break;

                    
    except Exception as e:
        #print('Exception: ', e)
        #print('no data from', addr)
        time.sleep(1)       
# Clean up the connection.
conn.close()
print("closed. ") 

