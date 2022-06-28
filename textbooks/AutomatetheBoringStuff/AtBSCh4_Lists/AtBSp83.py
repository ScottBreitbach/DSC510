catNames = []
x = 0
numCats = int(input('How many cats?: '))
while x < numCats:
    name = input('Enter name of cat ' + str(len(catNames) + 1) + ' (or enter nothing to stop.): ')
    if name == '':
        break
    catNames = catNames + [name]    # list concatenation
    x = x + 1
print('The cat names are: ')
for name in catNames:
    print('  ' + name)
