# main.py -- put your code here!
import usocket as socket
import time
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
c=""

while True: 
    if len(request1)>0:
        if flag==0:
            request2=request1.pop()
            request3=request2.split("\n")
            #print("request3")
            #print(request3)
            flag=1
        if flag==1:
            if len(request3)==0:
                flag=0
            else:
                request4=request3.pop(0)
                flag=2
        if flag==2:
            for a in request4:            
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
            #print(b[0])   
            #print(b[1])            
            #print(b[2])  
            flag=1
            conn.send("ok\r")
                
                
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