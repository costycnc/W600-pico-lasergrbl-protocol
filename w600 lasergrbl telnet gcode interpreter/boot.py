from time import sleep 
import network
wlan = network.WLAN(network.STA_IF)    
wlan.active(True)                      
wlan.connect("name", "psw")
for i in range(16):
	if wlan.isconnected():
		break
	else:
		sleep(.5)
if wlan.isconnected():
	print('Connected to', "name")
	import w600
	w600.run_ftpserver(port=21,username="user",password="12345678")
	sleep(1)
	print('URL:', wlan.ifconfig()[0]+':21', 'username: "user", password:"12345678"')
	print(wlan.ifconfig()[0])
import gc
gc.collect()
gc.mem_free()
