# Print Welcome Message
# variables should be descriptive

# message = """Bobby\'s World was a good
# cartoon in the 1990s"""

message = 'Hello World'
print(message)
print(len(message))
print(message[:5])
print(message[6:])
print(message.lower())          # or message.upper for uppercase
print(message.count('Hello'))   # counts instances of string argument
print(message.find('World'))    # World starts at the 6th index of message variable
                                # Returns -1 if string not found
new_message = message.replace('World', 'Universe')
print(new_message)              # prints Hello Universe

greeting = 'Hello'
name = 'Michael'
# message = greeting + ', ' + name + '. Welcome!'
message = '{}, {}. Welcome!'.format(greeting, name) # preferred
print(message)
