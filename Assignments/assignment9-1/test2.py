
# f = open('text.txt')

nameFile = input('pick a file name: ')
if nameFile[-4:] == '.txt':
    fileName = nameFile
else:
    fileName = nameFile + '.txt'

# print(nameFile[-4:])
# fileName = nameFile + '.txt'
# print(fileName[-4:])

# output_file = open(fileName, 'w')
print('File name is:', fileName)
try:
    with open(fileName, 'w') as f:
        f_contents = f.write('='.center(17, '=')+'\n'
                             'taco content\n')
        # f_contents = f.write('more stuff')
    # print(f_contents)
except Exception as e:
    print(e)
