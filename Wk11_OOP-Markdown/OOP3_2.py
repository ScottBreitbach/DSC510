'''Using class methods as alternative constructors'''

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

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# # Can parse the string every time...
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

# ...Or, could create an alternative constructor allowing
# to pass in the string and create the employee with @classmethod
new_emp_1 = Employee.from_string(emp_str_1) # provided a from_string alternative constructor

print(new_emp_1.email)
print(new_emp_1.pay)
