#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)

currentMem = 'members.txt'
exMem = 'inactive.txt'

def cleanFiles(currentMem,exMem):

    with open(currentMem, 'r+') as source_file:
        lines = source_file.readlines() 
        source_file.seek(0)
        
        for line in lines:
            if 'no' not in line:
                source_file.write(line)  
        
        source_file.truncate()

    with open(exMem, 'a') as inactive_file:
        for line in lines:
            if 'no' in line:
                inactive_file.write(line)

cleanFiles(memReg,exReg)