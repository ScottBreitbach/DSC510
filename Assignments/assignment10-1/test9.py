# course: DSC510
# assignment: 10.1
# date: 13-May-2020
# name: Scott Breitbach
# description: pulls a joke from the server upon user request.

import requests
import json
import textwrap

url = "https://api.chucknorris.io/jokes/random"

# List of affirmative responses to receive a joke:
affirmative = ['y', 'yes', 'yup', 'yea', 'yeah', 'sure', 'yuppers', 'yep',
               'please', 'affirmative', 'of course', 'ok', 'okay', 'fine']

# Function to try requesting a joke from the server:
def getTheJoke():
    try:
        response = requests.request("GET", url)
        try:            # checks for errors with response from server
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("\nSorry, the Internet might be broken!")
            errMsg(e)
        except Exception as e:
            errMsg(e)
        else:
            printTheJoke(response)
    except Exception as e:
        errMsg(e)

# Canned error message; provides error code:
def errMsg(err):
    print("\nIt looks like we didn't get the joke,\n"
          "but Chuck found the problem: ")
    print('>>', err)
    exit()

# Makes the joke "pretty" and prints it:
def printTheJoke(res):
    try:
        resString = json.loads(res.text)   # saves dictionary to variable
        # prints joke header in bold
        print('\n>> \033[1m'+"Here's your joke:\n"+'\033[0m',
              # prints joke, indented with wrapped text
              textwrap.indent(
                  textwrap.fill(resString['value'], width=50),
                  prefix='\t'))
    except Exception as e:
        errMsg(e)

# Main part of program that keeps the jokes coming, upon request:
def main():
    oneMore = input('\nYou want some more? [Y/N]: >> ')
    oneMore = oneMore.lower()
    if oneMore in affirmative:  # checks user response against list
        getTheJoke()            # and retrieves a joke if "yes"
        main()  # offers additional jokes
    else:
        print('\n>> Had enough, have you?'
              '\n>> Okay, Chuck will let you off easy this time.')
        exit()

# Welcome to the program:
print('Welcome to the Chuck Norris joke generator!')
initJoke = input('\nWould you like a Chuck Norris joke? [Y/N]: >> ')
initJoke = initJoke.lower()
if initJoke in affirmative:     # checks user response against list
    getTheJoke()                # and retrieves a joke if "yes"
    main()      # offers additional jokes
else:
    print("\n>> Really? You wouldn't like Chuck when he's angry.")
    exit()
