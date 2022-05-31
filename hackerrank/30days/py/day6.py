
even = []
odd = []

def rr(rin):
    print(len(rin))
    if(len(rin)> 2 and len(rin) <= 10000):
        #print(rin)
        i = 0
    
        while i < (int(len(rin))):
            if(i%2==0): even.append(rin[i])
            if(i%2==1): odd.append(rin[i]) 
            i+=1
        #print(even)
        #print(odd)
        e = str(even)
        e = e.replace('[','')
        e = e.replace(']','')
        e = e.replace(',','')
        e = e.replace(' ','')
        e = e.replace('\'','')
        print(e)
        o = str(odd)
        o = o.replace('[','')
        o = o.replace(']','')
        o = o.replace(',','')
        o = o.replace(' ','')
        o = o.replace('\'','')
        print(o)
    else:
        print("invalid length T")

test = input("enter a string: ")
rr(test)
