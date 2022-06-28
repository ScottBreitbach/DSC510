# course: DSC510
# assignment: 2.1
# date: 19-Mar-2020
# name: Scott Breitbach
# description: program that calculates the total cost of fiber optic
# cable based on number of feet purchased, then prints a receipt

print('Hello and welcome to the Fiber Optic Cable Ordering System (FOCOS)\n')
companyName = input('What Company are you representing today? ')
feetOfFiber = input('And how many feet of fiber optic cable will you need? ')
feetOfFiber = float(feetOfFiber)
installCost = feetOfFiber * 0.87  # calculate total cost of fiber installation
feetOfFiber = str(feetOfFiber)
installCost = str(installCost)

print('\n******************************\n'  # prints receipt
      + 'Thanks for shopping with FOCOS\n\n'
      + 'Bill To:\t' + companyName + '\n'
      + 'Material:\tFiber Optic Cable\n'
      + 'Quantity:\t' + feetOfFiber + ' ft\n'
      + 'Unit Price:\t$0.87/ft\n\n'
      + feetOfFiber + ' feet x $0.87/ft\n'
      + 'Your total today is $' + installCost + '\n'
      + '******************************')
