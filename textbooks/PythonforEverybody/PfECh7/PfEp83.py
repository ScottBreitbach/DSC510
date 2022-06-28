'''search for (and print) lines that start with "From"'''

# fhand = open('mbox.txt')
# for line in fhand:
#     if line.startswith('From:'):
#         print(line)

# note: this doubles up the \n from the file and from print()
# to remove, could slice last character, but
# easier to use 'rstrip' to strip whitespace from right side of string:

# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

'''can structure loop to follow pattern of skipping uninteresting lines'''

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    # Skip 'uninteresting' lines:
    if not line.startswith('From:'):
        continue
    # Process our 'interesting' line:
    print(line)
# output is the same
