import csv
import time
from datetime import datetime
'''
Input: it will get the value of the input filed and a the name of the database
Processing: It will search for the value in its respective database and if value is there then it wil return Its Id
else it will retuen the New Id for the new user
Output: It either return the ID of the field or will return the new ID for the new user. 
'''
def findData(name,fName):
    counter=1
    with open(fName,'r') as file:
        file = csv.reader(file)
        for i in file:
            if i[1] == name:
                return i[0],None
            counter+=1
    return None,counter

def writeData(arr,fName):
    with open(fName,'a',newline='') as file:
        file = csv.writer(file)
        file.writerow(arr)

start = time.time()
with open('test.csv','r') as file:
    file = csv.reader(file)
    for i in file:
        inTime = time.time()
        if "-" not in i:
            uid, userCounter = findData(i[0], 'userName.csv')
            gid, groupCounter = findData(i[2], 'userGroup.csv')
            wid, webCounter = findData(i[1], 'website.csv')
            if not uid:
                writeData([userCounter, i[0]], 'userName.csv')
            if not gid:
                writeData([groupCounter, i[2]], 'userGroup.csv')
            if not wid:
                writeData([webCounter, i[1]], 'website.csv')
            writeData(
                [time.time() - inTime , uid and uid or userCounter, gid and gid or groupCounter, wid and wid or webCounter],
                'finalData.csv')
        else:
            uid, userCounter = findData(i[0], 'userName.csv')
            gid, groupCounter = findData(i[2], 'userGroup.csv')
            wid, webCounter = findData(i[1], 'website.csv')
            writeData(
                [time.time() - inTime, uid and uid or userCounter, gid and gid or groupCounter,
                 wid and wid or webCounter,"One of the value is missing"],
                'finalData.csv')

print(time.time() - start)