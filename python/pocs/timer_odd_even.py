import time,os

def ranger():
    for x in range(1,20): 
        if x % 2 == 0: print(f"{x} is even") #nothing else yet 
        if x % 2 == 1: print(f"{x} is odd")
        time.sleep(.1) 
        os.system("cls") # clear screen for next number

def timer(n):
    for x in range(1,n):
        print(x)
        time.sleep(.51)
        os.system("cls")
os.system("cls")
timer(5)
ranger()

