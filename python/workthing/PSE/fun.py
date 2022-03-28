import time,os

os.system("cls")
for x in range(1,20): 
    if x % 2 == 0: print(f"{x} is even") #nothing else yet 
    if x % 2 == 1: print(f"{x} is odd")
    time.sleep(1) 
    os.system("cls") # clear screen for next number