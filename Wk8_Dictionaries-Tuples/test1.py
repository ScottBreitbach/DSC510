
person = {'name': 'Jenn', 'age': 23}
test = 'cool'
print(type(test))
print(test)

print(f'My name is {person["name"]} and I am {person["age"]:.2f} years old.')
test2 = f'My name is {person["name"]} and I am {person["age"]} years old.'
print(type(test2))
print(2, test2)

print('My name is', person['name'], 'and I am', person['age'], 'years old.')
test3 = 'My name is', person['name'], 'and I am', person['age'], 'years old.'
test3_2 = 'My name is', person['name'], 'and I am', str(person['age']), 'years old.'

print(type(test3))
print(3, test3)

test4 = 'My name is {name} and I am {age:.2f} years old.'.format(**person)
print(4, test4)

print(f'This is {test}')

test5 = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(5, test5)

person['name'] = 'John'
print(person['name'])
print(2, test2, type(test2))
print(3, test3, type(test3))
print(3.2, test3_2, type(test3_2))
print(4, test4, type(test4))
print(5, test5, type(test5))

print(person['name'])
