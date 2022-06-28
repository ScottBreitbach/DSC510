'''Python Class Inheritance'''
'''create different types of employees'''


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    # what if we want the developers to have a raise of 10%:
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        # # could also do:
        # Employee.__init__(self, first, last, pay) # super is more inheritable,
        # # a bit more maintainable when using multiple inheritance (future vid)


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
# dev_1 = Employee('Corey', 'Schafer', 50000)
dev_2 = Developer('Test', 'User', 60000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(help(Developer))

# print(dev_1.email)
# print(dev_2.email)
