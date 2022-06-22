import os
import shutil

source=input("enter the name of the source: ")
destination=input("enter the name of the destination path")
source=source+'/'
destination=destination+'/'
listOfFiles=os.listdir(source)

for file in listOfFiles:
    shutil.copy((source+file),destination)