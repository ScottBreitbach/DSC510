# course: DSC510
# assignment: 4.1
# date: 31-Mar-2020
# name: Scott Breitbach
# description: program that calculates the total cost of fiber optic
# cable based on number of feet purchased including a discount,
# if applicable, then prints a receipt. Now with defined functions!

def costCalc(feet, price):
    '''Calculates total cost of install'''
    return round((feet*price), 2)

def unitPrice(ft):
    '''Calculates price per foot with discount, if applicable'''
    if ft > 500:
        return 0.50
    elif ft > 250:
        return 0.70
    elif ft > 100:
        return 0.80
    else:
        return 0.87

print('Hello and welcome to the Fiber Optic Cable Ordering System (FOCOS)\n')
companyName = input('What Company are you representing today? ')
feetOfFiber = input('And how many feet of fiber optic cable '
                    'will you need installed? ')
try:
    feetOfFiber = float(feetOfFiber)
except:
    print('* Error: Please enter a numerical value. *')
    feetOfFiber = input('How many feet of fiber optic cable will you need '
                        'installed? ')
    try:
        feetOfFiber = float(feetOfFiber)
    except:
        print('* Error: This field requires a numerical value,'
              ' please begin again. *')
        exit()

pricePerFoot = unitPrice(feetOfFiber)
installCost = costCalc(feetOfFiber, pricePerFoot)

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
