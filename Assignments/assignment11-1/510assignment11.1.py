# course: DSC510
# assignment: 11.1
# date: 20-May-2020
# name: Scott Breitbach
# cash register program which keeps track of
# number of items and total cost at checkout

import time
import locale
locale.setlocale(locale.LC_ALL, '')
# provides local currency symbol for use in program:
locCurSym = dict(locale.localeconv())['currency_symbol']

class CashRegister:
    '''main cash register program for keeping track of purchases at checkout'''
    def __init__(self):         # constructor
        self.totalPrice = 0
        self.itemCount = 0

    def addItem(self, price):   # running total of item number and cost
        self.price = price
        self.totalPrice += price    # running total price
        if price >= 0:          # adds to item count when positive price
            self.itemCount += 1
            return "{} added to your cart"\
                .format(locale.currency(self.price, grouping=True))
        else:                   # removes from item count when negative price
            self.itemCount -= 1
            return "{} removed from your cart"\
                .format(locale.currency(self.price, grouping=True))

    @property
    def getTotal(self):         # returns total price of items in cart
        return ">> Your current total comes to: {}"\
            .format(locale.currency(self.totalPrice, grouping=True))

    @property
    def getCount(self):         # returns count of items in the cart
        return ">> You currently have {} items in your cart.".format(self.itemCount)

    @property
    def receipt(self):         # prints items and total on receipt upon Completion
        return "\tItems: {}\n"\
               "\tTotal: {}"\
            .format(self.itemCount, locale.currency(self.totalPrice, grouping=True))

def printLine(symbol, length):
    '''prints lines for welcome message and receipt'''
    print(symbol.center(length, symbol))

def register():
    '''cash register program : responds to user input'''
    decision = input("Please enter item price: {} ".format(locCurSym))
    try:                        # checks to see if number was entered
        decision = float(decision)
        print(checkout.addItem(decision))
    except:                     # handles non-numeric commands
        decision = decision.lower()
        if decision == 'c':     # Complete transaction
            print('')
            printLine('=', 30)
            print("RECEIPT".center(30))
            printLine('=', 30)
            print(checkout.receipt)
            printLine('-', 30)
            print("Thanks, please come again!".center(30))
            printLine('=', 30)
            exit()
        elif decision == 't':   # current Total price
            print(checkout.getTotal)
        elif decision == 'n':   # current Number of items
            print(checkout.getCount)
        else:                   # display help (command options)
            helpMsg()
    register()

def helpMsg():
    '''provides instructions for user input and proceeds to cash register'''
    print("At any time:\n"
          "\tEnter 'C' to Complete your transaction.\n"
          "\tEnter 'T' for your current Total.\n"
          "\tEnter 'N' to see the Number of items in your cart.\n"
          "\tEnter a negative value to remove item from cart.\n"
          "\tEnter anything else to see this help message again.\n")
    time.sleep(1)
    register()

def main():
    '''instantiates object, prints welcome message, and proceeds to instructions'''
    global checkout
    checkout = CashRegister()
    printLine('=', 55)
    print("Welcome to the Cash Register".center(55))
    print("We're ready when you are!".center(55))
    printLine('=', 55)
    time.sleep(2)
    helpMsg()

if __name__ == '__main__':
    main()
