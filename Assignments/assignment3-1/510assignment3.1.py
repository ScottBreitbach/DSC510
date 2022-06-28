# course: DSC510
# assignment: 3.1
# date: 25-Mar-2020
# name: Scott Breitbach
# description: program that calculates the total cost of fiber optic
# cable based on number of feet purchased, including a discount,
# if applicable, then prints a receipt

print('Hello and welcome to the improved Fiber Optic Cable Ordering System (FOCOS)\n')
companyName = input('What Company are you representing today? ')
feetOfFiber = input('And how many feet of fiber optic cable will you need installed? ')
try:
    feetOfFiber = float(feetOfFiber)
except:
    print('* Error: Please enter a numerical value. *')
    feetOfFiber = input('How many feet of fiber optic cable will you need installed? ')
    feetOfFiber = float(feetOfFiber)

if feetOfFiber > 500:
    pricePerFoot = 0.50
elif feetOfFiber > 250:
    pricePerFoot = 0.70
elif feetOfFiber > 100:
    pricePerFoot = 0.80
else:
    pricePerFoot = 0.87

installCost = feetOfFiber * pricePerFoot
round(installCost, 2)

print('\n******************************\n'  # prints receipt
      + 'Thanks for shopping with FOCOS\n\n'
      + 'Bill To:\t', companyName, '\n'
      + 'Material:\t Fiber Optic Cable\n'
      + 'Quantity:\t', feetOfFiber, ' ft')
if feetOfFiber > 100:
    print('Discounted')
print('Unit Price:\t$', '%.2f' % pricePerFoot, '/ft\n\n'
      + '[', feetOfFiber, 'ft x $', '%.2f' % pricePerFoot, '/ft ]\n'
      + 'Your total today is $', '%.2f' % installCost, '\n'
      + '******************************')
