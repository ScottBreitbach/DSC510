def loopFunction():
    number = input("type a number : ")
    try:
        number = float(number)
        return number
    except:
        print("that's not a number, try again")
        return loopFunction()

print("Your number is", loopFunction())
