# main.py -- put your code here!
import usocket as socket
import time
from machine import Timer 


s = socket.socket()
s.bind(('', 23))
s.listen(5)
conn, addr = s.accept()
#conn.setblocking(False)

x=0
request1=[]
flag=0
b=["0","0","0"]
d=9
g=0
c=""
request3=[]
targetx=0
targetxx=0
targety=0
actualx=0
actualy=0
ff=0

timer3 = Timer(3)
timer3.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:prt())

def prt():
    global flag
    global targetxx
    print("\n\r")
    print(targetxx)
    targetxx -=1
    if targetxx<0:
        flag=1
   
    

while True: 
    if len(request1)>0:
        if flag==0:
            request2=request1.pop(0)
            request3=request2.split("\n")
            #print("\n\r")
            #print("len(request3)=")
            #print(len(request3))
            flag=1
        if flag==1:
            #flag=2
            if len(request3)==0:
                flag=0
            else:
                request4=request3.pop(0)
                request4 +="n"
                for a in request4:                                 
                    if d in (0,1,2): 
                        if str(a) in ('-','0','1','2','3','4','5','6','7','8','9',' '):
                            c=c+str(a)
                        else:                             
                            b[d]=c                           
                            d="9" 
                            c=""                            
                    if str(a)=="X": d=0                         
                    if str(a)=="Y": d=1 
                    if str(a)=="G": d=2      
                if len(request1)<5:
                    conn.send("ok\r")                
                targetx =int(b[0])-ff
                targetxx=targetx
                #print("\n\r")
                #print(abs(targetx))
                ff=int(b[0])
                #targety +=int(b[1])
                flag=2
                                
                
                
    try:
        request = conn.recv(200)                
        if request:                 
            if "?" in request:   
                conn.send("<Idle|MPos:"+b[0]+","+b[1]+",0.000|FS:0,0>\r")
            else:
                request1.append(request.decode())                                             
    except Exception as e:
        #print('Exception: ', e)
        #print('no data from', addr)
        time.sleep(1)       
# Clean up the connection.
conn.close()
print("closed. ") 