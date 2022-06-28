'''how to format and print out numbers'''

# pad with zeros
for i in range (8, 11):
    sentence = 'The value is {}'.format(i)
    print(1, sentence)

for i in range (8, 11):
    sentence2 = 'The value is {:02}'.format(i)  # "zero" padding
    print(2, sentence2)


# change number of decimal places
pi = 3.14159265

sentence3 = 'Pi is equal to {:.2f}'.format(pi)  # :.nf to print to n decimal places
print(3, sentence3)


# add comma separators to large numbers for readability
sentence4 = '1 MB is equal to {} bytes'.format(1000**2)
print(4, sentence4)
sentence5 = '1 MB is equal to {:,} bytes'.format(1000**2)   # :, adds comma separators
print(5, sentence5)
sentence6 = '1 MB is equal to {:,.2f} bytes'.format(1000**2)   # can combine
print(6, sentence6)
