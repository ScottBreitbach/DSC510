'''Try Except Example'''

# Check for potential error
# if the userInput isn't an Integer, catch the exception and print a message

userInput = input('Please enter an integer: ')
try:
    userInput = int(userInput)
except:
    print('The number you entered was not an integer')
    # Code here to alter execution because we do not want to keep going
