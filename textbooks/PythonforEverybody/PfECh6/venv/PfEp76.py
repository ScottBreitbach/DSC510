# Debugging

while True:
    line = input('> ')
    # if line[0] == '#':  # if blank line entered, no zero-th character and it errors
    # if line.startwith('#'):   # this didn't seem to work at all
    if len(line) > 0 and line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
