'''adding another called Manager'''

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
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    # add option to pass in a list of employees this Mgr supervises:
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # give the option to add or remove from list of employees supervised:
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # print off list of employees supervised:
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

mgr_1 = Manager('Sue','Smith', 90000, [dev_1])

# print(issubclass(Developer, Employee))  # True
# print(issubclass(Manager, Employee))    # True
# print(issubclass(Manager, Developer))   # False

# print(isinstance(mgr_1, Manager))   # prints True
# print(isinstance(mgr_1, Employee))  # also True
# print(isinstance(mgr_1, Developer)) # False

# print(mgr_1.email)
# mgr_1.print_emps()
#
# mgr_1.add_employee(dev_2)
#
# print(mgr_1.email)
# mgr_1.print_emps()
#
# mgr_1.rem_employee(dev_1)
#
# print(mgr_1.email)
# mgr_1.print_emps()
