'''uses method.lower() '''
# feeling = input('How are you? ')
# if feeling.lower() == 'great':
#     print('I feel great too.')
# else:
#     print('I hope the rest of your day is good.')

'''testing other methods'''
# print('12ab'.isalnum())     # True
# print('12'.isalnum())       # True
# print('12 ab'.isalnum())    # False
# print('12-ab'.isalnum())    # False

'''using isX() to validate user input'''
# while True:
#     age = input('Enter your age:')
#     if age.isdecimal():
#         break
#     print('Please enter a number.')

'''justifying text w/rjust(), ljust() and center()'''
# print('Hello'.rjust(15))
# print('Hello'.ljust(15, '*'))
# print('Hello'.center(15, '='))

'''print unicode chars (alt-codes)'''
# howMany = int(input("how many unicode chars? 1 to ... "))
# i = 0
# while i <= howMany:
#     print(f'{i} is {chr(i)}')
#     i +=1

'''title case'''
# titleTest = 'always look on the bright side of life'
# titleTest = titleTest.title()
# print(titleTest)

'''adding variables in strings'''
buoyant1 = 'wood'
buoyant2 = 'a duck'
print(buoyant1 + ' floats in water and so does ' + buoyant2)
# use format operators:
print('%s floats in water and so does %s' % (buoyant1, buoyant2))
# use a formatted string:
print('{} floats in water and so does {}'.format(buoyant1, buoyant2))
# use f strings
print(f'{buoyant1} floats in water and so does {buoyant2}')
