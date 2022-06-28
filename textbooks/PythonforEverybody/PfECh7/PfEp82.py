'''use for loop to read through and count lines of a file'''

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count += 1
print('Line Count:', count)


'''if the file isn't huge, you can read it all in one string'''

fhand = open('mbox.txt')
inp = fhand.read()
print('Length:', len(inp))

print(inp[:20])

# good idea to store the output of 'read' as a variable
# because each call to read exhausts the resource

fhand = open('mbox.txt')
print(len(fhand.read()))    # output length
print(len(fhand.read()))    # output 0

