'''How to create simple classes;
The difference between a class and an instance of that class;
How to initialize class attributes and create methods.'''

# Python Object-Oriented Programming

class Employee:
    def __init__(self, first, last, pay):
        self.first = first  # note you could use something like self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1)
# print(emp_2)

# # can manually add to each employee, but there's an easier way (__init__ method):
# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

# print('{} {}'.format(emp_1.first, emp_1.last))
# # instead, can put a method in the class that allows us to put this functionality in one place

print(emp_1.fullname())
# Here's what is actually going on in the background
print(Employee.fullname(emp_1))
