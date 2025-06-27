import os
import json
import sys
import shutil

# make sure number of arguments is correct
if(len(sys.argv)!=2):
    print("Usage: python delete.py folder-name")
    quit()

# grab the argument
folder = sys.argv[1]

data = {}
end = False

with open("data.json", "r") as file:
    data = json.load(file)

    # if we can't find the folder-name in data.json file, it probably doesn't exist, queue to exit program
    if(not folder in data["folders"]):
        print("Folder {0} does not exist".format(folder))
        end = True

    # otherwise remove it from data.json list
    else:    
        data["folders"].remove(folder)

# if queued to exist program, exit program
if end: 
    quit()

# rewrite data.json with the new list
with open("data.json", "w") as file:
    json.dump(data, file, ensure_ascii=False)


# copy the removed folder-name from Projects to Deleted-Projects and then delete the original
shutil.copytree("./Projects/"+folder, "./Archive/Deleted-Projects/"+folder)
shutil.rmtree("./Projects/"+folder)