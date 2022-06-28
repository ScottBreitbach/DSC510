'''now let's look at static methods'''

class Employee:

    raise_amt = 1.04
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
        self.pay = int(self.pay * Employee.raise_amt)
        # self.pay = int(self.pay * self.raise_amount)    # Either of these will work

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

# add a simple function that will take in a date
# and return whether or not that was a workday
    @staticmethod
    def is_workday(day):
        if (day.weekday() == 5) or (day.weekday() == 6): # Sat and Sun
            return False
        return True

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2016, 7, 10)    # Sunday, False
my_date = datetime.date(2016, 7, 11)    # Monday, True

print(Employee.is_workday(my_date))

