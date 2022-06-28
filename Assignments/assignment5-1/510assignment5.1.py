# course: DSC510
# assignment: 5.1
# date: 08-Apr-2020
# name: Scott Breitbach
# description: program which prompts the user for operations
# and then performs various calculations

def performCalculation(operation):
    '''takes a parameter and values and performs the calculation'''
    firstNumber = input("Please enter the first number: ")
    # I know you said not to use try blocks when calling int() or float(),
    # but I don't know how else to keep the wrong inputs from throwing errors.
    try:
        firstNumber = int(firstNumber)
    except:
        try:
            firstNumber = float(firstNumber)
        except:
            print("Invalid entry.")
            performCalculation(operation)
            return
    secondNumber = input("Please enter the second number: ")
    try:
        secondNumber = int(secondNumber)
    except:
        try:
            secondNumber = float(secondNumber)
        except:
            print("Invalid entry, please try again.")
            performCalculation(operation)
            return
    if operation == '+':
        result = firstNumber + secondNumber
    elif operation == '-':
        result = firstNumber - secondNumber
    elif operation == '*':
        result = firstNumber * secondNumber
    elif operation == '/':
        if secondNumber == 0:
            print("Sorry, cannot divide by zero.")
            return
        else:
            result = firstNumber / secondNumber
    else:
        print("Something went wrong, please begin again.")
        return
    print(firstNumber, operation, secondNumber, "=", result)

def calculateAverage():
    '''asks user how many numbers to average and averages them'''
    listToAverage = []
    howMany = input("How many numbers would you like to average?: ")
    try:
        howMany = int(howMany)
    except:
        print("Please enter a whole number.")
        calculateAverage()
        return
    while len(listToAverage) < howMany:
        number = input("#" + (str(len(listToAverage) + 1)) + " >> Enter number: ")
        try:
            number = int(number)
        except:
            try:
                number = float(number)
            except:
                print("Invalid input. Please try again.")
                calculateAverage()
                return
        listToAverage = listToAverage + [number]
    print('The average of these numbers is', (sum(listToAverage)/len(listToAverage)))

keepRunning = True
while keepRunning == True:  # Keeps the program running until user exits
    whichOne = input("Would you like to perform a calculation, get an average, or exit? >> ")
    if (whichOne == "perform a calculation" or whichOne == "calculation"):
        print("Which calculation would you like to perform?")
        operator = input("Please enter '+', '-', '*', or '/' >> ")
        if not (operator == '+' or operator == '-' or operator == '*' or operator == '/'):
            print("Invalid input. Please begin again.")
            continue
        performCalculation(operator)
    elif (whichOne == "get an average" or whichOne == "average"):
        calculateAverage()
    elif (whichOne == "exit"):
        print("See you next time!")
        keepRunning = False
    else:
        print("I'm sorry,", "\""+whichOne+"\"", "isn't a valid input.")
        continue
