from ipaddress import ip_address
import sys,time,pyAesCrypt,io,socket,itsdangerous,getopt


ip,port = '127.0.0.1',9999
buff = 'hcmshoxhsaosphohpo,sjzss;zjdsj,;SJ,js;gzjfj;gj8es489gy5c4cu548vh 4v50vh54vuv56v5e[5xd4x78x0101010104wvw\8348t\]c18254\]4553]h44i530if534o653o53o6h3c'
noop_sled = "\x90"*16
i = 100
buffer = buff[0:i]
def fuzzer():
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((ip, port))
                s.recv(1024)
                print("Fuzzing with {} bytes".format(len(buff) ))
                i+=100
                s.send(bytes(buff, "latin-1"))
                s.recv(1024)
        except:
            print("Fuzzing crashed at {} bytes".format(len(buff) ))
            print('ran out of bytes or crashed')
            sys.exit(0)
        time.sleep(0.5)
    
if(len(sys.argv) > 1):
    if sys.argv[1] == '-h':
            print('bof_cli.py -e -i <ip-address> -o <offset> ')
            print('bof_cli.py -f -i <ip>\nbof_cli,py -e <ip> -o <offset>')
            sys.exit()
  
    elif sys.argv[1] == "-f":
        print('fuzzing mode selected')
        try:
            ip = sys.argv[2]
        except IndexError:
            print('missing IP')
            exit()
        print(f"fuzzing {ip} starting at {i} bytes")   
    elif sys.argv[1] == ("-e"):
        print('exploit mode selected')
        print('checking args')
        try:
            offset = int(sys.argv[2])
        except IndexError:
            print('missing offset')
            exit()
        print(f"exploit with offset:{offset}")
    else:
        print('invalid selection ')
        print('bof_cli.py -f -i <ip>\nbof_cli,py -e <ip> -o <offset>')
        exit()

else:
    print('no args entered')
    print('bof_cli.py -f -i <ip>\nbof_cli,py -e <ip> -o <offset>')
    exit()
    
   