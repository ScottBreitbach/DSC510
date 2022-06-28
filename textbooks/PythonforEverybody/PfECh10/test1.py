'''replace ! with space using maketrans()'''
textInput = 'abc!def'
charRemove = '!'    # can use multiple chars here
charReplace = ' '   # and multiple chars here
newText = textInput.maketrans('', '', '!')              # just deletes '!'
print(textInput.translate(newText))

newText = textInput.maketrans(charRemove, charReplace)  # replaces '!' with ' '
print(textInput.translate(newText))

'''replace ! with space using replace()'''  # faster / easier
textInput = 'abc!def'
print(textInput)
textInput = textInput.replace('!', ' ')
print(textInput)
