numberHours = input('Enter your hours worked: ')
try:
    hours = float(numberHours)
except:
    print('Please enter a number')

hourlyRate = input('Enter your pay rate per hour: ')
try:
    rate = float(hourlyRate)
except:
    print('Please enter a number')

if hours <= 40.0:
    totalPay = hours * rate
    totalPay = str(totalPay)
    print('$' + totalPay + ' is your total pay')
