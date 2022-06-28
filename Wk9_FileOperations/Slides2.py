'''Writing to files'''


# Text to be written is contained in the variable textToWrite:
# with open(filePath, 'w') as fileHandle:     # w for writing
#     fileHandle.write(textToWrite)           # write out text from a variable


# Example:
fileName = 'programming.txt'

with open(fileName, 'w') as fileHandle:
    fileHandle.write("I love programming.")


# Appending instead:
fileName = 'programming.txt'

with open(fileName, 'a') as fileHandle:
    fileHandle.write("I love programming and Python.")
