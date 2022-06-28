'''Inheritance Example'''

# Definition of parent class Person

class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self): # Name function returns the firstName and lastName.
        return self.firstname + " " + self.lastname

# Definition of child class called Employee. Employee is a child of the Person
# class and derives behavior from the Person class.

class Employee(Person): # Notice the syntax here, for declaring a child class.
    def __init__(self, first, last, employeeNum): # When we declare an employee object
                                                  # we are instantiating an Employee
                                                  # class as well as a person class.
        Person.__init__(self, first, last)
        self.employeeNum = employeeNum

    def GetEmployee(self): # GetEmployee returns the Name of the employee as defined
                           # by the parent class and the employeeNum as defined
                           # by the Employee class
        return self.Name() + ", " + self.employeeNum

# Create an object of type Person
examplePerson = Person("Mark", "Zuckerberg")
# Create an object of type Employee
exampleEmployee = Employee("Bill", "Gates", "1983")

# Call the Name function from the Person class
print(examplePerson.Name())
# Call the GetEmployee function from the Employee class
print(exampleEmployee.GetEmployee())
