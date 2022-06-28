
filePath = 'testFile2.txt'
# with open(filePath, 'r') as fileHandle:     # r for reading
#     data = fileHandle.read()                # read into a variable
# print(data)

try:
    with open(filePath, 'w') as fileHandle:
        pass
    #     data = fileHandle.read()
    # print(data)
except Exception as e:
    print(e)
