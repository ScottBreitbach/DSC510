'''use "find" string method to simulate text editor search string within lines'''

fhand = open('mbox.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue      # if str not found (i.e. == -1), continue
    count += 1
    print(line)
print(count)

