import usocket as socket
import time
s = socket.socket()
s.bind(('', 23))
s.listen(5)
conn, addr = s.accept()
#conn.setblocking(False)

x=0
 
while True:            
    try:
        request = conn.recv(200)                
        if request:                
            x +=1
            print("\r")
            print(x)             
            print(request)
            conn.send("ok\n")  
            if "?" in request:   
                conn.send("<Idle|MPos:0.000,0.000,0.000|FS:0,0>\r")
                x -=1            
    except Exception as e:
        #print('Exception: ', e)
        #print('no data from', addr)
        time.sleep(1)       
# Clean up the connection.
conn.close()
print("closed. ") 

