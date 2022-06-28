# # counts the # of letter 'a'
#
# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count += 1
# print(count)

def letterCounting(word, countedLetter):
    count = 0
    for letter in word:
        if letter == countedLetter:
            count += 1
    print('There are', count, 'letters', countedLetter)

wordRequested = input("Give me a word: ")
letterToCount = input("Which letter to count: ")
letterCounting(wordRequested, letterToCount)
