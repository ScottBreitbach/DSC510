'''Property Decorators: Getters, Sliders, & Deleters'''

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@company.com'

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Corey Schafer'

# emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)  # added method, need to add parentheses but that's not what we want
# print(emp_1.email())
# print(emp_1.fullname())
print(emp_1.fullname)   # add @property and you don't need the parentheses

del emp_1.fullname

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
