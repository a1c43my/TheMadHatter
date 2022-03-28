import os,sys,time,re
from part import *


pars_list = []
readData = open("log.html","r");
#readData = open("test.txt","r");
#readData = open("PARS_GMT_001_017.html","r");
keepreading = True
while keepreading:
    read1 = str(readData.readline())
    if read1:
        
        if(read1.__contains__("PAR_Recurrence") and read1.__contains__("logentry")): 
            
            t1 = str(re.findall("PAR\_Recurrence\_\(Closed\)|PAR\_Recurrence\_\(Open\)",read1))
            t2 = str(re.findall("logentry[0-9]{7}",read1))
            if len(t1) > 0 and len(t2) > 0: 
                print(f"PAR entry found in {t2}, {t1} \n")
        for par in open_pars:
            if read1.__contains__(par):
                print(f"open par {par}")
                pars_list.append(par)
        for par in clsd_pars:
            if read1.__contains__(par):
                print(f"closed par {par}")
                pars_list.append(par)
        #if (read1.__contains__("logentryspacer")): print(f"ending logentry::")
    elif not read1: 
        print('end of file')
        keepreading=False;

morning_report = open('morning_report.txt','a')
for rep in report:
    if (rep in open_pars or rep in clsd_pars): 
        print(f"Adding Summary for {rep} add to file")
       
        morning_report.write(f"GMT 2022/xxx {rep} \n")
        morning_report.write(f"- - - - - - - - - - - - - - - - - -\n")
        morning_report.write(f"- - - - - - - - - - - - - - - - - -\n")
        print(f"PAR Summary for {rep} added to file")
morning_report.close()
#print(report['MUSES-SW-0018'])