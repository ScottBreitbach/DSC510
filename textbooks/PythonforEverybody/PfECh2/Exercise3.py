hourly = input('How many hours then?\n')
print(hourly + ' hours you say')
ratePerHour = input('Yeah okay but how bout the rate?\n')
print(ratePerHour + ' dollarinos per hour huh')
hourly = int(hourly)
ratePerHour = int(ratePerHour)
pay = (hourly * ratePerHour)
pay = str(pay)
print('I guess that\'s $' + pay + ' you got yourself there')
