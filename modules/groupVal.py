import csv
from fileinput import FileInput
def userGroup(name, group):
    with open('usergroup.csv','r') as file:
        counter =1
        file = csv.reader(file)
        for i in file:
            if i[1] == name and (group in i[2].split(',')):
                return 1,None
            elif i[1] == name and (group not in i[2].split(',')):
                return 2,", ".join(i[2].split(','))
            else:
                counter+=1
                continue
    with open('usergroup.csv','a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([counter, name, group])
    return 0,[]

def ugroupAppend(name, group):
    flag = 0
    temp = ''
    with open('usergroup.csv','r') as file:
        file = csv.reader(file)
        for i in file:
            if i[1] == name and (group in i[2].split(',')):
                return 1
            elif i[1] == name and (group not in i[2].split(',')):
                if len(i[2].split(',')) > 1:
                    flag = 1
                    temp = name + ',' + '"' +i[2]
                elif len(i[2].split(',')) == 1:
                    flag = 2
                    temp = name + ',' + i[2]
                break
            else:
                flag = 3
    if flag!=3:
        with FileInput('usergroup.csv', inplace=True, backup='.bak') as inp:
            if flag ==1:
                print(temp)
                for i in inp:
                    print(i.replace(temp + '"', temp + ',' + group + '"'), end='')
            elif flag == 2:
                for i in inp:
                    print(i.replace(temp, temp[:len(name)+1] + '"' + temp[len(name)+1:] + ',' + group + '"'), end='')
            return 2
    else:
        return 0

def ugroupReplace(name, group):
    flag = 0
    temp = ''
    with open('usergroup.csv', 'r') as file:
        file = csv.reader(file)
        for i in file:
            if i[1] == name and (group in i[2].split(',')):
                return 1
            elif i[1] == name and (group not in i[2].split(',')):
                if len(i[2].split(',')) > 1:
                    temp = name + ',' + '"' + i[2] + '"'
                elif len(i[2].split(',')) == 1:
                    temp = name + ',' + i[2]
                break
            else:
                flag = 3
    if flag != 3:
        print(temp)
        with FileInput('usergroup.csv', inplace=True, backup='.bak') as inp:
            for i in inp:
                print(i.replace(temp, temp[:len(name)+1] + group), end='')
            return 2
    else:
        return 0
