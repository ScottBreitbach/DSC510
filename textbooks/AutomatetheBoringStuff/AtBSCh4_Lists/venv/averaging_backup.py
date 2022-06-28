def calculateAverage():
    '''asks user how many numbers to average and averages them'''
    howMany = input("How many numbers would you like to average? ")
    try:
        howMany = int(howMany)
    except:
        print("Please enter a whole number.")
        calculateAverage()
        return
    i = 0
    runningTotal = 0
    while i < howMany:
        userValue = input("Enter a number: ")
        if userValue == 'exit':
            return
        try:
            userValue = int(userValue)
        except:
            try:
                userValue = float(userValue)
            except:
                print("Invalid input, please begin again.")
                calculateAverage()
                return
        runningTotal = runningTotal + userValue
        i = i + 1
    print("The average is: ", runningTotal/howMany)
