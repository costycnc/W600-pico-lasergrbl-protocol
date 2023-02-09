import socket

s = socket.socket()
s.bind(('', 8000))
s.listen(5)
a=0
while True:
    conn, addr = s.accept() 
    request = conn.recv(1024)
    #request1 = request.decode()
    print(request)
    print(a)
    if a==0:	
        a=a+1
        print(a)
    if a==1:	
        conn.send("\r")
        conn.send("Grbl 1.1h ['$' for help]\r")
        conn.send("<Idle|MPos:0.000,0.000,0.000|FS:0,0|Pn:S|WCO:0.000,0.000,0.000>\r")
        a=a+1
    if a>1:
        conn.send("<Idle|MPos:0.000,0.000,0.000|FS:0,0|Pn:S>\r")
        a=a+1
        print(a)
    conn.close()		