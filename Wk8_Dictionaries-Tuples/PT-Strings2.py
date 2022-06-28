
class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(1, sentence)

# Can pass in keyword arguments to format
sentence2 = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
print(2, sentence2)

person = {'name': 'Jenn', 'age': 23}
sentence3 = 'My name is {name} and I am {age} years old.'.format(**person) # most readable / convenient
print(3, sentence3)

