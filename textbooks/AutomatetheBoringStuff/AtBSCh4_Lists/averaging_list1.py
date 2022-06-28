# listToAverage = []
# howMany = int(input("How many numbers to average?: "))
# while len(listToAverage) < howMany:
#     number = int(input((str(len(listToAverage)+1)) + " >> Enter number: "))
#     listToAverage = listToAverage + [number]
# print('Average is ' + str(sum(listToAverage)/len(listToAverage)))

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
    print('The average is', (sum(listToAverage)/len(listToAverage)))

calculateAverage()
