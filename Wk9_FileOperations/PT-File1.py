'''File Objects'''

# f = open('test.txt', 'r')
#
# print(f.name)
# print(f.mode)
#
# f.close()   # don't forget this part; just do it when you open the file

'''to open a file using a context manager'''
# will close file automatically upon exiting block of code
# will also close the file if an exception is thrown

with open('test.txt', 'r') as f:    # variable (f) is over on the right here
            # will stil have access to variable f after exiting loop, jsyk
    # pass
    f_contents = f.read()       # reads the entire contents of a file
    # f_contents = f.readlines()  # get a list of all of the lines in the file (incl \n chars)
    # f_contents = f.readline()   # prints the first line in the file then next line each time run after
    # print(f_contents, end='')   # with end='' , will no longer add in the newline
    # f_contents = f.readline()   # prints the next line in the file
    # print(f_contents, end='')
# print(f.closed)       # True

