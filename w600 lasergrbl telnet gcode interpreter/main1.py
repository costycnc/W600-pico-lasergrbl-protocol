# based mainly on https://www.youtube.com/watch?v=GVMuER7A770
#inspired from https://maker.pro/forums/threads/w600-pico-webserver.292684/


from machine import Pin

print("Connection successful")
#print(sta.ifconfig())

# setup the webserver
try:
    import usocket as socket
except:
    import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create new socket, address family type = AF_INET, socket type = SOCK_STREAM
s.bind(('', 80))
s.listen(5) # accept connections. backlog = 5 = max. number of unaccepted connections before refusing new connections

# interact with the hardware
led = Pin(Pin.PA_00, Pin.OUT, Pin.PULL_FLOATING)
led_off = 1 # inverted logic
led_on = 0

# web page data
def web_page():
    file = open("index.html", "r")
    page = file.read()
    file.close()
    return page
	
def rosso(arg):
    file = open("rosso.html", "r")
    page = file.read()
    file.close()
    return page


# this is the main loop to handle requests
while True:
    conn, addr = s.accept() # accept connection with a new socket object "conn" to remote address "addr"
    request = conn.recv(1024) # receive from connected socket "conn" using 1024 byte buffer
    request1 = request.decode()#https://mkyong.com/python/python-3-typeerror-cant-convert-bytes-object-to-str-implicitly/
    #myString = "one|two|three"
    #print(myString.split("|"))
    res1 = request1.split('\n')[0]
    res = res1.split(' ')
    print(res)
    if res[0]=="GET":
        resx=res[1].split('?')
        if resx[0]=="/index1.html":
            file = open("index1.html", "r")
            response = file.read()
            file.close() 
        elif resx[0]=="/rosso.html":
            if len(resx)==1:
                response="no arguments"
            else:
                response = resx[1]+"aaaa"
        else:
            file = open("index.html", "r")
            response = file.read()
            file.close()             
        print("res1="+res[1])
        print(res[1])		
        print("este get")
        resx=res[1].split('?')
        print(resx[0][1:]) 		
    if "GET /?led=off" in res:
        led.value(led_off)
    #print(request) # for debugging only
    if "GET /?led=on" in request:
        led.value(led_on)
    if "GET /?led=off" in request:
        led.value(led_off)
      
#    led_status = ("ON", "OFF") led.value() ==1 # this should be valid python code, too, but I prefer the better readable form below.
    if led.value == 1: # same as before but imho better readable
        led_status = "ON"
    else:
        led_status = "OFF"
    #response = web_page() % led_status # insert the actual status into the web page
    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Content-type: text /html\n")
    conn.send("Connection: close\n\n")
    conn.sendall(response)
    conn.close()