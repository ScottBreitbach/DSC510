def performCalculate(variableA, variableB, operator):
    if  operator == "+":
        total = variableA + variableB
    elif operator == "-":
        total = variableA - variableB
    elif operator == "*":
        total = variableA * variableB
    elif operator == "/":
        total = variableA / variableB
    else:
        print("You entered an invalid operator.")

    print("You entered ", variableA, " and ", variableB, " as well as the operator of ", operator)
    print("Your calculation is: ", total)
    return;

firstVariable = int(input("Please enter the first number: "))
secondVariable = int(input("Please endter another number: "))
operator = input("Please enter an operator: +, -, *, /: "
                 "")

performCalculate(firstVariable, secondVariable, operator)
