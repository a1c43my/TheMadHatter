import socket,time,os

HOST = '127.0.0.1'
PORT = 2048
PORTa = 2049
BUFFER_SIZE = 4096
SEPARATOR = "-"
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.bind((HOST,PORT))
print('server listening')
a.listen(5)
connection,address = a.accept()

#print(connection)
#print(address)
dd = str(connection)
#print(dd.split())
#print(f'connection establsihed from : {address}') #f is for printing

while True:
    data = connection.recv(1024)
    if data.decode() == 'alive':
        print(data)
        time.sleep(1)
        print(f'connection establsihed from : {address[0]}') #f is for printing
        connection.send('exe'.encode())
    elif data.decode() == 'load':
        print('malware executed')
        time.sleep(1)
        print('sending sleep')
        connection.send('sleep'.encode())
    elif data.decode().__contains__('bot'):
        print('sending sleep ')
        time.sleep(1)
        connection.send('sleep'.encode())
    
    else:        
  
        print(data.decode())
        msg = 'standard'   
        time.sleep(1)
        connection.send(msg.encode())
