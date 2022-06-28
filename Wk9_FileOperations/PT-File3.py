'''writing to files'''

# with open('test.txt', 'r') as f:
#     f.write('Test')         # get an error if you try to write in a read mode

# with open('test2.txt', 'w') as f:   # open a file in write mode
#     # pass
#     f.write('Test')
#     f.seek(0)
#     f.write('R')

'''let's pull all this together and use read & write on multiple files at the same time'''

with open('test.txt', 'r') as rf:   # rf here is a reference to read file
    with open('test_copy.txt', 'w') as wf:  # write file (note: these can be on same line separated by comma
        for line in rf:
            wf.write(line)  # write each line in rf file to wf file
