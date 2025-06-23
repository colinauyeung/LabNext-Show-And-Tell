import csv
import os
import json
from datetime import datetime

header = []

with open('NewEntries.csv', newline="") as csvfile:
    re = csv.reader(csvfile)
    for i,row in enumerate(re):
        if(i == 0 ):
            header = row
            continue

        badges = [row[4]]
        for i in range(5,8):
            print(i)
            if(len(row[i])>0):
                badges.append(row[i])

    
        res = {
            "ImageFile": row[2],
            "Badges": badges,
            "Title": row[0],
            "Author": row[1]
        }
        mypath = "Projects/" + row[3]
        if not os.path.isdir(mypath):
            os.makedirs(mypath)

        with open(mypath+"/info.json", "w", encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False)

        data = {}
        with open("data.json", "r") as file:
            data = json.load(file)
            print(data)
            if row[3] not in data["folders"]:
                data["folders"].append(row[3])

        with open("data.json", "w") as file:
            json.dump(data, file, ensure_ascii=False)

        os.rename(row[2], mypath+"/"+row[2])

        print(res)

todaystr = datetime.today().strftime('%Y-%m-%d')
os.rename("NewEntries.csv", "Archive/Entered-"+todaystr+".csv")

with open('NewEntries.csv', "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()


print(datetime.today().strftime('%Y-%m-%d'))
