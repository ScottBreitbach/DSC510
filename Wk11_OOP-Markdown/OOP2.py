'''Class variables (as opposed to instance variables)
and when you would use each one'''

class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first  # note you could use something like self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * 1.04)
        self.pay = int(self.pay * Employee.raise_amount)
        # self.pay = int(self.pay * self.raise_amount)    # Either of these will work

print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)

# Employee.raise_amount = 1.05
# emp_1.raise_amount = 1.05

# print(emp_1.__dict__)   # prints the dictionary of available attributes
# print(Employee.__dict__)    # class does contain the raise_amount attribute

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
#
# print(emp_2.__dict__)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

