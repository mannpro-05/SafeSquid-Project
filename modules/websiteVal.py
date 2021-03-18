import pandas as pd
from datetime import datetime
import csv
def websiterEnter(name, website):
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S %d/%m/%Y")
    with open('usergroup.csv','r') as file:
        counter =1
        file = csv.reader(file)
        for i in file:
            if i[1] == name:
                with open('website.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([dt_string,i[0],website])
                return 1,0
            else:
                counter+=1
                continue
    with open('usergroup.csv','a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([counter, name, 'temp'])
    with open('website.csv','a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([dt_string, counter, website])
    return 0, counter