'''Dictionaries and key-value pairs
aka hash maps or associative arrays'''

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)
print(student['name'])
# print(student['phone'])     # not a key so throws an error, use get instead
print(student.get('name'))
print(student.get('phone'))     # returns None instead of an error
print(student.get('phone', 'Not Found'))  # can pass if value if nothing is returned

'''add phone number to student dictionary'''
student['phone'] = '555-5555'
student['name'] = 'Jane'        # can update values using key
print(student)

'''do a bunch of updates in one shot'''
student.update({'name': 'Juan', 'age': 26, 'phone': '555-4444'})
print(student)

'''delete a specific key and it's value'''
# del student['age']              # removes a value
age = student.pop('age')        # removes and returns value
print(student)
print(age)
