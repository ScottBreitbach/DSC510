'''format and print out dates'''

import datetime
myDate = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(1, myDate)

# March 01, 2016        see Directive on python.org for codes
# %B for Month; %d for day number; %Y for year
sentence = '{:%B %d, %Y}'.format(myDate)
print(2, sentence)

# March 01, 2016 fell on a Tuesday and was the 061 day of the year.
# %A for weekday; %j for day of year
sentence2 = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year.'.format(myDate)
    # need 0 index because of three placeholders
print(3, sentence2)
