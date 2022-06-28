'''OS Path and File Processing Example'''

import os           # import the OS library

filePath = '/users/micha/PycharmProjects/Wk9_FileOperations/'
fileName = 'testFile.txt'
completePath = filePath+fileName

if os.path.isfile(fileName):        # check if file exists
    print('File Exists')
if os.path.isdir(filePath):         # check if file path exists
    print('Directory Exists')
if os.path.exists(completePath):    #check if complete path exists
    print('Complete Path Exists')
print('Complete Path', completePath)
with open(completePath, 'w') as fileHandle:             # open file for writing
    fileHandle.write("I love programming and Python (and tacos).")  # write data to file
with open(completePath, 'r') as fileHandle:             # open same file for reading
    data = fileHandle.read()                            # read data from the file
    print(data)
