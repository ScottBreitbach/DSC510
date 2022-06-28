'''Reading File Example'''

# Opening and reading a file using "with" will create a file object (fileHandle in this case)
filePath = 'testFile.txt'
with open(filePath, 'r') as fileHandle:     # r for reading
    data = fileHandle.read()                # read into a variable
print(data)

# Opening and reading a file without "with"
filePath = 'testFile.txt'
fileHandle = open(filePath, 'r')            # r for reading
data = fileHandle.read()                    # read into a variable
fileHandle.close()                          # if you don't open using 'with' you must close the file!
print(data)
