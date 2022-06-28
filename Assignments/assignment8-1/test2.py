# course: DSC510
# assignment: 8.1
# date: 29-Apr-2020
# name: Scott Breitbach
# description: program which processes the Gettysburg text, counting
# instances of each word and prints them in order from most to least

import string
wordCounts = {}

'''Adds individual words to a dictionary and counts instances of those words'''
def add_word(wordFromLine):
# def add_word(wordFromLine, wordCountDict):
    # if word in wordCoundDict:
    #     wordCountDict[word] += 1
    if wordFromLine not in wordCounts:  # checks if word is missing from dictionary
        wordCounts[wordFromLine] = 1    # adds new word to dictionary and gives count of 1
    else:
        wordCounts[wordFromLine] += 1   # increments count of existing word by 1

'''Strips lines of punctuation and creates uniform case for letters'''
def process_line(lineOfText):
# def process_line(lineOfText, wordCountDict):
    # lineOfText = lineOfText.strip()   # didn't seem to do anything so I commented it out
    lineOfText = lineOfText.translate(lineOfText.maketrans('', '', string.punctuation))
                                        # removes punctuation from lines of text
    lineOfText = lineOfText.lower()     # makes text uniformly lowercase
    words = lineOfText.split()          # splits line of text into list of words
    for word in words:
        add_word(word)
        # add_word(word, wordCountDict)

'''Prints the total number of unique words as well as a list of the words and their counts 
from most to least frequent. Formats width of printout based on width of initial string.'''
def pretty_print(wordDict):
    dictStr = 'Unique words: ' + str(len(wordDict))
                                        # assigns string to a variable for function & width
    printLine('=', len(dictStr))        # calls printLine function to print a line
    print(dictStr)
    printLine('=', len(dictStr))
    print('Word'.ljust(len(dictStr)-7) + 'Count'.rjust(7))
                                        # prints headers for columns
    printLine('-', len(dictStr))
    wordList = []
    for word, count in wordDict.items():
        wordList.append((count, word))  # adds counts, words from dictionary to a list
    wordList.sort(reverse=True)         # sorts list by counts
    for count, word in wordList:
        count = str(count)
        print(word.ljust(len(dictStr)-4, '.') + count.rjust(4, '.'))
                                        # formats and prints words, counts
    printLine('=', len(dictStr))

'''Prints a line of specified character based on length of string'''
def printLine(symbol, length):
    print(symbol.center(length, symbol))

'''Opens file and calls other functions to process text and print results'''
def main():
    # wordCounts = {}
    try:
        gba_file = open('gettysburg.txt', 'r')
        for line in gba_file:
            process_line(line)          # processes each line of text file
            #process_line(line, wordCounts)
    except:
        print('Error: File could not be opened.')
        exit()
    # print('length of dictionary', len(wordCountDict))
    pretty_print(wordCounts)            # print results

if __name__ == "__main__":
    main()
