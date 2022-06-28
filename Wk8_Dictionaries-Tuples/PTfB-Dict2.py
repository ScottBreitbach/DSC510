'''loop through keys and values of a dictionary'''

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(len(student))         # prints number of key-value pairs
print(student.keys())       # prints just the keys
print(student.values())     # prints just the values
print(student.items())      # prints the key-value pairs

for key in student:
    print(key)

for key, value  in student.items():
    print(key, value)
