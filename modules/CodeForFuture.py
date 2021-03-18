import pandas as pd

def userGroup(name, group):
    df = pd.read_csv('usergroup.csv')
    if len(df.loc[df['uname'] == name]) == 0:
        df = df.append({'uid': str(len(df) + 1),
                        'uname': name,
                        'ugroup': group}, ignore_index=True)
        df.to_csv('usergroup.csv', index=False)
        return 0, []  # this means that no such entry is there and the data is appended to the csv file

    else:
        existingUgroups = df.loc[df['uname'] == name]['ugroup'].to_string(index=False).strip().split(',')

        if group in existingUgroups:
            return 1, []  # This means that the userame already exists and the username is also present.
        else:
            return 2, df.loc[df['uname'] == name]['ugroup'].to_string(
                index=False).strip()  # this means that the user is there but the usergroup is new.
def append():
    if len(df.loc[df['uname'] == name]) == 0:
        return 0#this means that the user is not there.

    else:
        existingUgroups = df.loc[df['uname'] == name]['ugroup'].to_string(index=False).strip().split(',')
        if group in existingUgroups:
            return 1# this means that the user is there and also belongs to same usergrop i.e. the data is already there in the csvFile

        else:
            index = df.loc[df['uname'] == name].index.tolist()
            df.loc[index[0], 'ugroup'] += ','+group
            df.to_csv('usergroup.csv', index=False)
            return 2#Data is appended to the usergroup.
def ugroupReplace(name, group):
    df = pd.read_csv('usergroup.csv')

    if len(df.loc[df['uname'] == name]) == 0:
        return 0  # this means that the user is not there.

    else:
        existingUgroups = df.loc[df['uname'] == name]['ugroup'].to_string(index=False).strip().split(',')
        if group in existingUgroups:
            return 1# this means that the user is there and also belongs to same usergrop i.e. the data is already there in the csvFile
        else:
            index = df.loc[df['uname'] == name].index.tolist()
            df.loc[index[0], 'ugroup'] = group
            df.to_csv('usergroup.csv', index=False)

            return 2  # Data is appended to the usergroup.

def websiterEnter(name, website):
    dfUser = pd.read_csv('usergroup.csv')
    dfWebsite = pd.read_csv('website.csv')
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S %d/%m/%Y")
    if len(dfUser.loc[dfUser['uname'] == name]) == 0:
        dfUser = dfUser.append({'uid': str(len(dfUser) + 1),
                   'uname': name,
                   'ugroup': 'temp'}, ignore_index=True)
        dfUser.to_csv('usergroup.csv', index=False)

        uid = dfUser.loc[dfUser['uname'] == name]['uid'].to_string(index=False)
        dfWebsite = dfWebsite.append({
            'time': dt_string,
            'uid': uid,
            'website': website
        }, ignore_index=True)
        dfWebsite.to_csv('website.csv', index=False)

        return 0, uid
    else:
        dfWebsite = dfWebsite.append({
            'time': dt_string,
            'uid': dfUser.loc[dfUser['uname'] == name]['uid'].to_string(index=False),
            'website': website
        }, ignore_index=True)
        dfWebsite.to_csv('website.csv', index=False)

        return 1,0


    with open('userName.csv','r') as userName:
        userName = csv.reader(userName)
        for userData in userName:
            if userData[1] == name:
                with open('finalData.csv','r') as finalData:
                    finalData = csv.reader(finalData)
                    for rows in finalData:
                        if rows[1] == userData[0]:
                            groupId = rows[2].split(',')
                            with open('userGroup.csv','r') as userGroup:
                                userGroup = csv.reader(userGroup)
                                for groupData in userGroup:
                                    for id in groupId:
                                        if groupData[0] == id:
                                            return {'error':'1','message' : 'The username and the usergroup already exist'}
                return {'error': '1',
                        'message': 'The user \'' + name + '\' already belongs to the userGroup\'' + ",".join(
                            rows[2].split(',')) + '\'. So if you want to append or replace the existing '}


def userName1(name):
    logging.warning('hello')
    data = {}
    finalJson = {}
    temp = []
    with open('userName.csv', 'r') as file:
        file = csv.reader(file)
        for i in file:
            if i[1][:len(name)] == name:
                uname = ''
                timestamp = ''
                webname = ''
                group = ''
                with open('finalData.csv', 'r') as finalData:
                    finalData = csv.reader(finalData)
                    for rows in finalData:
                        if rows[1] == i[0]:
                            uname = csvReader.findUnameDisplay(i[0],uname)
                            group = csvReader.findUgroupDisplay(rows[2], group)
                            webname = csvReader.findWebsiteDisplay(rows[3], webname)
                            timestamp += rows[0]+','
                temp.append([i[0], uname[:-1], group[:-1], webname[:-1], timestamp[:-1]])

    data["DATA"] = temp
    data["COLUMNS"] = [{"title": "UserID"}, {"title": "UserName"}, {"title": "UserGroup"}, {"title": "WebsiteName"},
                       {"title": "TimeStamp"}]
    finalJson["data"] = data
    return finalJson

def userGroup(group):
    flag = 0
    logging.warning('hello')
    data = {}
    finalJson = {}
    temp = []
    with open('userGroup.csv', 'r') as file:
        file = csv.reader(file)
        for i in file:
            if i[1] == group:
                with open('finalData.csv', 'r') as finalData:
                    finalData = csv.reader(finalData)
                    for rows in finalData:
                        uname = ''
                        timestamp = ''
                        webname = ''
                        if rows[2] == i[0]:
                            uname = csvReader.findUnameDisplay(rows[1],uname)
                            webname = csvReader.findWebsiteDisplay(rows[3], webname)
                            timestamp += rows[0]+','
                            for j in range(len(temp)):
                                if temp[j][1] == uname[:-1]:
                                    temp[j][3] += ','+webname[:-1]
                                    temp[j][4] += ','+timestamp[:-1]
                                    flag = 1
                                    break
                            if flag == 1:
                                continue
                            else:
                                temp.append([rows[1], uname[:-1], group, webname[:-1], timestamp[:-1]])

    data["DATA"] = temp
    data["COLUMNS"] = [{"title": "UserID"}, {"title": "UserName"}, {"title": "UserGroup"}, {"title": "WebsiteName"},
                       {"title": "TimeStamp"}]
    finalJson["data"] = data
    print(finalJson)
    return finalJson