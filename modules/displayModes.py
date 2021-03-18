import csv
import inspect
from modules import app
from modules.readCsv import csvReader
from datetime import datetime
from modules.displayModule import displayFunctions
import json
'''
1.Input: The first one is the formdata which is the data coming out of the form and second one is mappingList which is a 
dict which contains the ID's of the corresponding fields.
2.Processing:The function will do a lot of filtering(according to data,time,username.usergrtoup etc) based on the data 
which is received form the formData.
3.Output:It would be a json format data witch will contain all the data which is to be displayed after the processing
/filtering part is complete. 
'''
def groupingDisplay(formData = {}, mappingList = {}):

    tempRows ={}
    finalVal = []
    now = datetime.now()
    app.logger.info(
        str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][
            3] + ':Arr ' + json.dumps(formData) + ' Fname: ' + json.dumps(mappingList))
    with open('finalData.csv', 'r') as finalData:
        finalData = csv.reader(finalData)
        if mappingList["getAllData"]:
            for rows in finalData:
                tempRows["timestamp"] = rows[0]
                tempRows["userName"] = rows[1]
                tempRows["userGroup"] = rows[2]
                tempRows["website"] = rows[3]
                now = datetime.now()
                app.logger.info(
                    str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][
                        3] + ':tempRows ' + json.dumps(tempRows) + ' Rows: ' + ','.join(rows))
                opt = displayFunctions.getAllData \
                    (tempRows, formData["fields"])
                if opt:
                    while ("" in opt[0]):
                        opt[0].remove("")
                    finalVal.append(opt[0])
                    temp = opt[1]
            return displayFunctions.outputReturn(temp, finalVal)
        if formData["starttime"] == "" and formData["startdate"] == "":
            for rows in finalData:
                tempRows["timestamp"] = rows[0]
                tempRows["userName"] = rows[1]
                tempRows["userGroup"] = rows[2]
                tempRows["website"] = rows[3]
                now = datetime.now()
                app.logger.info(
                    str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][
                        3] + ':tempRows ' + json.dumps(tempRows) + ' Rows: ' + ','.join(rows))
                opt = displayFunctions.gettingBasics\
                    (tempRows, mappingList, formData["fields"])
                now = datetime.now()
                app.logger.info(
                    str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][
                        3] + ' OPT: ' )
                if opt:
                    while ("" in opt[0]):
                        opt[0].remove("")
                    finalVal.append(opt[0])
                    temp = opt[1]
            return displayFunctions.outputReturn(temp, finalVal)



        elif formData["starttime"] != "" and formData["startdate"] == "":
            for rows in finalData:
                if rows[0].split()[0] >= formData["starttime"] and rows[0].split()[0] <= formData["endtime"]:
                    tempRows["timestamp"] = rows[0]
                    tempRows["userName"] = rows[1]
                    tempRows["userGroup"] = rows[2]
                    tempRows["website"] = rows[3]
                    opt = displayFunctions.gettingBasics \
                        (tempRows, mappingList, formData["fields"])

                    if opt:
                        while ("" in opt[0]):
                            opt[0].remove("")
                        finalVal.append(opt[0])
                        temp = opt[1]
            if finalVal:
                return displayFunctions.outputReturn(temp, finalVal)
            else:
                return displayFunctions.outputReturn({}, finalVal)

        elif formData["startdate"] != "" and formData["starttime"] == "":
            for rows in finalData:
                if rows[0].split()[1] >= formData["startdate"] and rows[0].split()[1] <= formData["enddate"]:
                    tempRows["timestamp"] = rows[0]
                    tempRows["userName"] = rows[1]
                    tempRows["userGroup"] = rows[2]
                    tempRows["website"] = rows[3]
                    opt = displayFunctions.gettingBasics \
                        (tempRows, mappingList, formData["fields"])

                    if opt:
                        while ("" in opt[0]):
                            opt[0].remove("")
                        finalVal.append(opt[0])
                        temp = opt[1]
            if finalVal:
                return displayFunctions.outputReturn(temp, finalVal)
            else:
                return displayFunctions.outputReturn({}, finalVal)
        else:
            for rows in finalData:
                if (rows[0].split()[0] >= formData["starttime"] and rows[0].split()[0] <= formData["endtime"]) \
                    and (rows[0].split()[1] >= formData["startdate"] and rows[0].split()[1] <= formData["enddate"]):
                    tempRows["timestamp"] = rows[0]
                    tempRows["userName"] = rows[1]
                    tempRows["userGroup"] = rows[2]
                    tempRows["website"] = rows[3]
                    opt = displayFunctions.gettingBasics \
                        (tempRows, mappingList, formData["fields"])

                    if opt:
                        while ("" in opt[0]):
                            opt[0].remove("")
                        finalVal.append(opt[0])
                        temp = opt[1]
            if finalVal:
                return displayFunctions.outputReturn(temp, finalVal)
            else:
                return displayFunctions.outputReturn({}, finalVal)