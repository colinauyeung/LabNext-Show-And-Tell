import csv
import os
import json
from datetime import datetime

header = []
added = []

# Open the CSV file
with open('NewEntries.csv', newline="") as csvfile:
    re = csv.reader(csvfile)

    # Iterate through the rows
    for i,row in enumerate(re):

        # Save the first row as the header data and then skip it
        if(i == 0 ):
            header = row
            continue

        # Grab all the badges
        badges = [row[4]]
        for i in range(5,8):
            print(i)
            if(len(row[i])>0):
                badges.append(row[i])

    
        # Create the json for info.json for the info for the slide
        res = {
            "ImageFile": row[2],
            "Badges": badges,
            "Title": row[0],
            "Author": row[1]
        }

        # Make the project directory if it doesn't exist
        mypath = "Projects/" + row[3]
        if not os.path.isdir(mypath):
            os.makedirs(mypath)

        # Make and write the info.json for the project
        with open(mypath+"/info.json", "w", encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False)

        # Check to see if the project folder is listed in data.json
        # if not, save an updated list to a local variable
        data = {}
        with open("data.json", "r") as file:
            data = json.load(file)
            # print(data)
            if row[3] not in data["folders"]:
                data["folders"].append(row[3])


        # and then write it back to data.json
        with open("data.json", "w") as file:
            json.dump(data, file, ensure_ascii=False)

        # move the image file to the project folder
        os.rename(row[2], mypath+"/"+row[2])

        # keep track of the added projects
        added.append(row[3])


print("Added {0}: ".format(len(added)), end="")
for name in added:
    print(name, end=", ")
print("")

# If we add new projects
if(len(added)>0):

    # move the current NewEntries.csv to the archive with a timestamp and make a clean copy
    todaystr = datetime.today().strftime('%Y-%m-%d')
    os.rename("NewEntries.csv", "Archive/Entered-"+todaystr+".csv")

    with open('NewEntries.csv', "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()



# print(datetime.today().strftime('%Y-%m-%d'))
