from modules.readCsv import csvReader
from modules import app
import json
import inspect
from datetime import datetime
def gettingBasics(rows, mappingList,fields):
    temp = {}
    temp["uid"] = ""
    temp["userName"] = ""
    temp["userGroup"] = ""
    temp["website"] = ""
    temp["timestamp"] = ""
    flag = 1
    now = datetime.now()
    app.logger.info(
        str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3] + ':' + json.dumps(
            rows)+' MappingList:'+json.dumps(mappingList)+' fields:'+','.join(fields))
    for key, val in mappingList.items():
        if key != 'getAllData':
            if rows[key] == mappingList[key]:
                continue
            else:
                flag = 0
                break
    if flag == 1:
        for key,val in rows.items():
            now = datetime.now()
            app.logger.info(
                str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3] + ':' + 'key:' + key + 'value:'+ val)
            if key in fields:
                if key == 'timestamp':
                    temp[key] = rows[key]
                else:
                    data = csvReader.findDataDisplay(rows[key],(key+'.csv'))
                    if data != None:
                        temp[key] = data
                if 'uid' in fields:
                    temp['uid'] = rows["userName"]
        return [temp["uid"], temp["userName"], temp["userGroup"], temp["website"], temp["timestamp"]], temp


def getAllData(rows,fields):
    temp = {}
    temp["uid"] = ""
    temp["userName"] = ""
    temp["userGroup"] = ""
    temp["website"] = ""
    temp["timestamp"] = ""
    for key, val in rows.items():
        now = datetime.now()
        app.logger.info(
            str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][
                3] + ':' + 'key:' + key + 'value:' + val)
        if key in fields:
            if key == 'timestamp':
                temp[key] = rows[key]
            else:
                data = csvReader.findDataDisplay(rows[key], (key + '.csv'))
                if data != None:
                    temp[key] = data
            if 'uid' in fields:
                temp['uid'] = rows["userName"]
    return [temp["uid"], temp["userName"], temp["userGroup"], temp["website"], temp["timestamp"]], temp


'''
Input: username, group, webname, timestamp will be the strings which will contain the data which is to be displayed on
the webpage!
Processing: It will convert the input strings into JSON format data in a specific format such that it fits in the frontend
Output: It will return the JSON format data.
'''
def outputReturn(temp, fdata):
    data = {}
    finalJson = {}
    columns = []
    now = datetime.now()
    print(type(temp), type(fdata))
    app.logger.info(str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3] + ':temp' + json.dumps(temp) +' Fdata:' + ','.join([str(i) for i in fdata]))
    if temp != {}:
        for key,val in temp.items():
            if temp[key] != "":
                columns.append({"title":key})
        now = datetime.now()
        app.logger.info(
            str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3] + ':temp' + ','.join([str(i) for i in columns]) + ' Fdata:' + ','.join([str(i) for i in fdata]))
        data["COLUMNS"] = columns
        now = datetime.now()
        app.logger.info(
            str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3] + ' Fdata:' + ','.join([str(i) for i in fdata]))
        data["DATA"] = fdata
        finalJson["data"] = data
        now = datetime.now()
        app.logger.info(
            str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3] + ':temp' + json.dumps(
                finalJson) + ' Fdata:' + ','.join([str(i) for i in fdata]))

        with open('modules/static/data.json', 'w') as file:
            json.dump(finalJson,file)
        return finalJson
    data["DATA"] = []
    data["COLUMNS"] = [{"title": "UserID"}, {"title": "UserName"}, {"title": "UserGroup"},
                       {"title": "WebsiteName"},{"title":"TimeStamp"}]
    finalJson["data"] = data
    return finalJson




