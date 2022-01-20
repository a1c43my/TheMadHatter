import os,sys,time,re

#readData = open("log.html","r");
readData = open("test.txt","r");
keepreading = True
while keepreading:
    read1 = str(readData.readline())
    if read1:
        
        if(read1.__contains__("PAR_Recurrence") and read1.__contains__("logentry")): 
            
            t1 = str(re.findall("PAR\_Recurrence\_\(Closed\)|PAR\_Recurrence\_\(Open\)",read1))
            t2 = str(re.findall("logentry[0-9]{7}",read1))
            if len(t1) > 0 and len(t2) > 0: 
                print('reading line with PAR')
                print(f"PAR entry found in {t2}, {t1} \n") 
    elif not read1: print('end of file');keepreading=False;