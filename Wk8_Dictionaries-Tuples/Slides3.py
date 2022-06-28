'''Count words in a string program'''

# Create a string which stores the phrase:
speech = 'to be or not to be'
# Split the speech string into a list where each word is an item in the list:
speechList = speech.split()
# Create a dictionary called wordCountDict:
wordCountDict = {}

# We are going to use the following logic to create the list:
# We are going to use a for loop to iterate through the list
# If the word (from the list) doesn't exist in the dictionary we are
# going to create a key-value pair for the word
# The key-value pair will have the word (from the list) as the key and
# the number of times the word appears in the list as the value
# If the word does exist, we will create a key in the dictionary
# and increment the value by 1.

# Iterate through each word in the list:
for word in speechList:
    # If the word is in the dictionary then we need to increment the
    # value associated with the key (ie the word from the string)
    if word in wordCountDict:
        wordCountDict[word] += 1
    # If the word doesn't exist in the dictionary then we need to
    # add 1 to the value associated with the key
    else:
        wordCountDict[word] = 1

# Print out the dictionary:
print(wordCountDict)
