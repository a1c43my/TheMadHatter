import re

#list of summaries for the report
open_pars = [
    'AMS-SW-0021','ASTROBEE-HW-0003','ASTROBEE-SW-0004',
    'Bioculture-SW-0003','Bioculture-SW-0004',
    'CAL-HW-0009','CAL-HW-0010','CAL-HW-0011','CAL-HW-0012','CAL-HW-0013',
    'Celestial-Immunity-HW-0001',
    'CIR-HW-0046','CIR-HW-0047','CIR-HW-0050','CIR-HW-0052','CIR-HW-0053','CIR-HW-0054',
    'ECOSTRESS-SW-0012','ECOSTRESS-SW-0013',
    'ELC3-SW-0003',
    'EXPRESS-HW-0006','EXPRESS_Laptop-SW-0005',
    'ExpRk3-SW-0034','ExpRk3-SW-0037','ExpRk3-SW-0039',
    'ExpRk4-SW-0081','ExpRk4-SW-0082',
    'ExpRk5-SW-0012','ExpRk5-SW-0013','ExpRk5-SW-0014','ExpRk5-SW-0015',
    'ExpRk6-HW-0011',
    'ExpRk8-SW-0019',
    'ExpRk9B-SW-0002','ExpRk9B-SW-0006',
    'FIR-SW-0034','FIR-SW-0035','FIR-SW-0039','FIR-SW-0040',
    'GEDI-SW-0005','GEDI-SW-0008','GEDI-SW-0009'





]
clsd_pars = []
report = {
    'MUSES-SW-0018':'record for MUSES-SW-0018',
    'STPH5-SW-0008':'record for STPH5-SW-0008',
    'EXPRESS_B-SW-0001':'record for EXPRESS_B-SW-0001',
    'ExpRk2-SW-0071':'record for ExpRk2-SW-0071',
    'MUSES-SW-0013':'record for MUSES-SW-0013',
    'ExpRk6-SW-0002':'record for ExpRk6-SW-0002',
    'NREP-SW-0007':'record for NREP-SW-0007',
    'MSG-HW-0012':'record for MSG-HW-0012',
    'MOCHII-SW-0002':'record for MOCHII-SW-0002',
    'MERLIN1-SW-0002':'empty',
    'MSG-SW-0051':'empty',
    'SAMS-SW-0008':'empty',
    'TSIS-SW-0006':'empty',
    'test':'record for test '
    }

getPARS = open("ALL_PARS.csv",'r')
keepreading = True
while keepreading:
    read1 = str(getPARS.readline())
    if read1:
        #t3 = read1.split(',')
        #print(t3[2]) #the alias
        #print(t3[5]) # the status
        #if str(t3[5]) == "CLOSED": clsd_pars.append(t3[2])
        #t2 = str(re.findall("OPENED",t3))
        #if t3[5] == "OPENED": open_pars.append(t3[2])
        #if t3[5] == "CLOSED": clsd_pars.append(t3[2])
        if read1.__contains__('CLOSED'):
            for r in report:
                find_it = str(re.findall(r,read1))
                if len(find_it) > 0: 
                    #print(f"CLOSED PAR: {find_it}")
                    find_it = find_it.replace('[','')
                    find_it = find_it.replace(']','')
                    if report[r]:
                        #print(report[r])
                        clsd_pars.append(find_it)
        if read1.__contains__('OPENED'):
            for r in report:
                find_it = str(re.findall(r,read1))
                if len(find_it) > 0: 
                    #print(f"OPEN PAR: {find_it}")
                    find_it = find_it.replace('[','')
                    find_it = find_it.replace(']','')
                    open_pars.append(find_it)
    elif not read1: 
        
        print('end of file')
        keepreading=False;
        

print(clsd_pars)
print(open_pars)