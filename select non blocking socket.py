import usocket as socket
import uselect as select

def do_something_else():
    #The other script to be executed besides of the blocking socket

def Client_handler(client_obj):
    #Do this when there's a socket connection

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 5000))
server.listen(5)

while True:
    r, w, err = select.select((server,), (), (), 1)
    if r:
        for readable in r:
            client, client _addr = server.accept()
        try:
            Client_handler(client)
        except OSError as e:
            pass
    do_something_else()
