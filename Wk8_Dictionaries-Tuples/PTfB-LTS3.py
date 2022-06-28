
courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses.index('CompSci'))     # provide index of value
print('Art' in courses)             # tells if value is in list
print()
for item in courses:
    print(item)

'''print each index number and item in list, starting at 1 (instead of 0)'''
for index, course in enumerate(courses, start=1):
    print(index, course)

'''join lists to string and split strings to list'''

courseStr = ', '.join(courses)      # creates one string, separated by commas
print(courseStr)

newList = courseStr.split(', ')     # turns string into a list
print(newList)
