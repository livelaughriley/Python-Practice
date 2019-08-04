import sys
import os

source = "./temp/"
destination = "./tempdest/"
extension = ".sh"
fileList = []

for root, folders, files in os.walk(source):
    for f in files:
        fileName, fileExtension = os.path.splitext(os.path.join(root, f))
        if (fileExtension == extension):
            fileList.append(os.path.join(root, f))

for f in fileList:
    os.rename(f, destination + f.split('/')[-1])
