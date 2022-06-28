'''better way to go through lines of a file'''

# with open('test.txt', 'r') as f:

    # for line in f:              # can run through the whole file this way
    #     print(line, end='')


'''another way to read through the whole file'''

# Repeat reading chunks of characters:
# with open('test.txt', 'r') as f:

#     f_contents = f.read(100)    # prints the first 100 characters of file
#     print(f_contents, end='')
#     f_contents = f.read(100)    # prints the next 100 characters of the file (picks up where left off)
#     print(f_contents, end='')


# Use a loop that reads through chunks of characters:
# with open('test.txt', 'r') as f:
#
#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#
#     print(f.tell())             # tells you what position in the file you are at

    # while len(f_contents) > 0:
        # print(f_contents, end='*')  # will print a * every 10 char (if size_to_read is 10) to visualize loop working
        # f_contents = f.read(size_to_read)


# Something else going on here, idk:
with open('test.txt', 'r') as f:

    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    f.seek(0)                           # 0 to start at beginning, but can start wherever you like
    f_contents = f.read(size_to_read)   # what if we want this second f.read to start back at beginning? f.seek:
    print(f_contents, end='')

