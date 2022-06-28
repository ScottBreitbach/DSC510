'''Easter eggs'''

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':    # <-- this part here
        print('oh, you got me!')
        exit()
    else:
        print('File cannot be opened:', fname)
        exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count +=1
print('There were', count, 'subject lines in', fname)
