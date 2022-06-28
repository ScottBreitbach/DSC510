'''access values from dictionaries and lists'''
person = {'name': 'Jenn', 'age': 23}
print('person:', person)

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(1, sentence)

sentence2 = 'My name is {} and I am {:.2f} years old.'.format(person['name'], person['age'])
print(2, sentence2)

tag = 'h1'
text = 'This is a headline'
sentence3 = '<{0}>{1}</{0}>'.format(tag, text)  # tag will go to 0s, text to 1s
print(3, sentence3)

sentence4 = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(4, sentence4)
sentence5 = 'My name is {0[name]} and I am {1[age]} years old.'.format(person, person) #second person is redundant
print(5, sentence5)
sentence6 = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(6, sentence6)

l = ['Jenn', 23]
sentence7 = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)
print(7, sentence7)

person['name'] = 'John'
print(person)
print(1, sentence, type(sentence))
print(2, sentence2, type(sentence2))
print(4, sentence4, type(sentence4))
print(5, sentence5, type(sentence5))
print(6, sentence6, type(sentence6))
print(person)

