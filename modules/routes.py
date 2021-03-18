from flask import *
from modules import app
from modules import displayModes, inputAllData, mapping
import inspect
from datetime import datetime
import json
from modules.mailDict import sendMail, mailUpdate
import csv
@app.route('/')
def index():
    now = datetime.now()
    app.logger.info(str(now.strftime("%H:%M %Y-%m-%d"))+ ' '+ __file__ + ' ' +inspect.stack()[0][3])
    return render_template('userDetails.html', disable='disable',
                               hidden='hidden', err='')
@app.route('/display')
def display():
    now = datetime.now()
    app.logger.info(str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3])
    return render_template('display1.html')

@app.route('/config')
def config():
    now = datetime.now()
    app.logger.info(str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3])
    with open('modules/config.json') as configFile:
        config_data = json.load(configFile)
        return render_template('mailConfig.html', smtp=config_data["MAIL_SERVER"], port=config_data["MAIL_PORT"], \
                               email=config_data["MAIL_USERNAME"], password=config_data["MAIL_PASSWORD"])
'''
1.input: It is a json data which is coming from the Input form.
2.processing: Calling a function which will store the data
3.output: A json message saying Data entered successfully!!!
'''
@app.route('/save', methods=['GET', 'POST'])
def writeCSV():
    if request.method == 'POST':
        data = request.get_json()
        now = datetime.now()
        app.logger.info(str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3]+':'+json.dumps(data))
        inputAllData.insertAllData(data["uname"], data["ugroup"], data["website"])
        return {'message':'Data enterd successfully!!!'}

'''
1.input: It is a json data which is coming from the querying form.
2.processing: Calling a mapping function which will do the mapping part and then will validate the input. Once the validation
is done then if will go to the displaying part where filtering will be done on the basis of the input from the user. 
3.output: It would be a json format data witch will contain all the data which is to be displayed after the processing
/filtering part is complete.
'''
@app.route('/returnData', methods=['GET','POST'])
def returnData():

    if request.method == 'POST':
        data = request.get_json()
        session['data'] = data
        if 'data' in session:
            now = datetime.now()
            app.logger.info(
                str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3] + ':' + json.dumps(
                    data))
            arr = mapping.mappingList(data)
            now = datetime.now()
            app.logger.info(
                str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3] + ':' + json.dumps(
                    arr))
            if arr != {}:
                temp = displayModes.groupingDisplay(data, arr)
                now = datetime.now()
                app.logger.info(
                    str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][
                        3] + ':' + json.dumps(
                        temp))
                if data["email"] != "":
                    sendMail.sendMail(data["email"], temp)
                    return temp
                return temp
            else:
                return {"data":{
                    "data": [],
                    "COLUMNS": [{"title": "UserID"}, {"title": "UserName"}, {"title": "UserGroup"}, {"title": "WebsiteName"},
                       {"title": "TimeStamp"}]
                }}


@app.route('/mailConfig', methods=['GET','POST'])
def mailConfig():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        session['data'] = data
        if 'data' in session:
            mailUpdate.mailConfig(data)
            return {"message":"The mail server has been updated!"}

@app.route('/displayDefault', methods=['GET','POST'])
def displayDefalut():
    print(request.method)
    if request.method == 'POST':
        data = request.get_json()
        temp = displayModes.groupingDisplay(data,mappingList={"getAllData":True})
        return temp



























'''@app.route('/append', methods=['GET', 'POST'])
def append():
    if request.method == 'POST':
        uname = request.form['uname']
        group = request.form['ugroup']

        result = groupVal.ugroupAppend(uname, group)
        if result == 0:
            disable = 'disabled'
            hidden = 'hidden'
            err = 'Username is not there in the data base. Please enter the user first!'
            return redirect(url_for('hello_world', disable=disable, hidden=hidden, err=err))
        elif result == 1:
            disable = 'disabled'
            hidden = 'hidden'
            err = 'Username and userGroup already Exits!'
            return redirect(url_for('hello_world', disable=disable, hidden=hidden, err=err))
        else:
            disable = 'disabled'
            hidden = 'hidden'
            err = 'Usergroup '+ group + ' has been appended successfully!'
            return redirect(url_for('hello_world', disable=disable, hidden=hidden, err=err))

@app.route('/replace', methods=['GET', 'POST'])
def replace():
    if request.method == 'POST':
        uname = request.form['uname']
        group = request.form['ugroup']
        result = groupVal.ugroupReplace(uname, group)
        if result == 0:
            disable = 'disabled'
            hidden = 'hidden'
            err = 'Username is not there in the data base. Please enter the user first!'
            return redirect(url_for('hello_world', disable=disable, hidden=hidden, err=err))
        elif result == 1:
            disable = 'disabled'
            hidden = 'hidden'
            err = 'Username and userGroup already Exits!'
            return redirect(url_for('hello_world', disable=disable, hidden=hidden, err=err))
        else:
            disable = 'disabled'
            hidden = 'hidden'
            err = 'Usergroup '+ group + ' has been replaced successfully!'
            return redirect(url_for('hello_world', disable=disable, hidden=hidden, err=err))
'''



