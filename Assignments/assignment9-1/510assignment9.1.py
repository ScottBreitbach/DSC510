# course: DSC510
# assignment: 9.1
# date: 08-May-2020
# name: Scott Breitbach
# description: program which processes the Gettysburg text, counting instances of
# each word and prints to a file, named by the user, in order from most to least.

import string
import re
wordCounts = {}

'''Adds individual words to a dictionary and counts instances of those words'''
def add_word(wordFromLine):
    if wordFromLine not in wordCounts:  # checks if word is missing from dictionary
        wordCounts[wordFromLine] = 1    # adds new word to dictionary and gives count of 1
    else:
        wordCounts[wordFromLine] += 1   # increments count of existing word by 1

'''Strips lines of punctuation and creates uniform case for letters'''
def process_line(lineOfText):
    # lineOfText = lineOfText.strip()   # didn't seem to do anything so I commented it out
    lineOfText = lineOfText.translate(lineOfText.maketrans('', '', string.punctuation))
                                        # removes punctuation from lines of text
    lineOfText = lineOfText.lower()     # makes text uniformly lowercase
    words = lineOfText.split()          # splits line of text into list of words
    for word in words:
        add_word(word)

'''Prints to file the total number of unique words as well as a list of the words 
and their counts from most to least frequent.'''
def process_file(wordDict, f_n):
    with open(f_n, 'a') as output_file:
        output_file.write('\n' + 'Word'.ljust(10) + 'Count'.rjust(7) +
                          '\n' + '-'.center(17, '-'))
        wordList = []
        for word, count in wordDict.items():
            wordList.append((count, word))
        wordList.sort(reverse=True)
        for count, word in wordList:
            count = str(count)
            output_file.write('\n' + word.ljust(13, '.') + count.rjust(4, '.'))
        output_file.write('\n' + '='.center(17, '='))

'''Opens file and calls other functions to process text and print results'''
def main():
    try:
        gba_file = open('gettysburg.txt', 'r')
        for line in gba_file:
            process_line(line)          # processes each line of text file
        gba_file.close()
    except:
        print('Error: File could not be opened.')
        exit()
    # Request file name from user and apply file extension:
    nameFile = input('What would you like your file to be called?: ')
    if nameFile[-4:] == '.txt':         # in case user includes file extension
        fileName = nameFile
    else:
        fileName = nameFile + '.txt'
    # Check file name for special characters:
    regex = re.compile("[@!#$%^&*()<>?/\\\|}{~:]")
    if regex.search(fileName) == None:
        try:
            with open(fileName, 'w') as output_file:    # creates output file
                output_file.write('='.center(17, '=')+  # word count header to file
                                  '\n' + 'Unique words: ' + str(len(wordCounts)) +
                                  '\n' + '='.center(17, '='))
        except Exception as e:
            print('Error:', e)
            exit()
    else:
        print('Special characters [@!#$%^&*()<>?/\|}{~:] not accepted.\n'
              'Please try again.')
        exit()
    process_file(wordCounts, fileName)          # exports word count data to file
    print('Data exported to file:', fileName)   # provides file name to user

if __name__ == "__main__":
    main()
