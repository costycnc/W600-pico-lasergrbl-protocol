#inspired from https://maker.pro/forums/threads/w600-pico-webserver.292684/

#create access point
import easyw600 
easyw600.createap(ssid="W600_softAP") 
#create ftp server ( can be manipulate with dos ftp or the free ftp https://filezilla-project.org/
import w600 
w600.run_ftpserver(port=21,username="user",password="user") 

# setup the webserver
try:
    import usocket as socket
except:
    import socket
