import csv
import inspect
from modules import app
from datetime import datetime
'''
Input: it will get a list of data which is supposed to be inserted in the database and also the name of the database.
Processing: It will just insert the list into the database
Output: It will not return anything 
'''
def writeData(arr,fName):
    now = datetime.now()
    app.logger.info(
        str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][
            3]  + ' Fname: ' + fName)

    with open(fName,'a',newline='') as file:
        file = csv.writer(file)
        file.writerow(arr)

