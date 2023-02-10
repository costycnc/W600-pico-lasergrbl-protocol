import usocket as socket
import time

s = socket.socket()
s.bind(('', 23))
s.listen(5)
conn, addr = s.accept()
conn.setblocking(False)
a=0
while True:
    try:
        request = conn.recv(10)
        a=a+1       
        if request:
            print(request)
        else:
            print('No data: connection closed by the client')
            break;
        if b"\x18" in request:
            a=0
        if a==3:
            conn.send("\n")     
            conn.send("Grbl 1.1h ['$' for help]\r") 
        if a==4:    
            conn.send("<Idle|MPos:0.000,0.000,0.000|FS:0,0|WCO:0.000,0.000,0.000>\r")
        if a==5:    
            conn.send("<Idle|MPos:0.000,0.000,0.000|FS:0,0|Ov:100,100,100>\r")      
        if a==6:    
            conn.send("<Idle|MPos:0.000,0.000,0.000|FS:0,0>\r")         
        if "$" in request:    
            conn.send("ok\r")                        
        if "G" in request:    
            conn.send("ok\r")                 
    except Exception as e:
        print('Exception: ', e)
        print('no data from', addr)
        time.sleep(1)       
# Clean up the connection.
conn.close()
print("closed. ")
