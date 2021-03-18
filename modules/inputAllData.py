from modules.readCsv import csvReader
from modules.writeCsv import csvWriter
from datetime import datetime
'''
1.Input: The username, usergroup and website are the input ot the function which are to be entered into the database

2.Processing: The input will be checked if the values are already there in the database. If they are there then
simply the ID will returned which will be used to store in the finalData database. If they are not there then
a new ID will be created and the records will be stored in the database.

3.Output:This function has no output.
'''
def insertAllData(name,group,website):
    now = datetime.now()
    dt_string = now.strftime("%H:%M %Y-%m-%d")
    uid,userCounter = csvReader.findData(name,'userName.csv')
    gid,groupCounter = csvReader.findData(group,'userGroup.csv')
    wid, webCounter = csvReader.findData(website,'website.csv')
    if not uid:
        csvWriter.writeData([userCounter,name], 'userName.csv')
    if not gid:
        csvWriter.writeData([groupCounter,group], 'userGroup.csv')
    if not wid:
        csvWriter.writeData([webCounter, website], 'website.csv')
    csvWriter.writeData([dt_string, uid and uid or userCounter,  gid and gid or groupCounter, wid and wid or webCounter],'finalData.csv')





