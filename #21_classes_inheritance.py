class Person():

    def __init__(self, name):
        self.name = name
        self.surname = "Goodenough"
        self.age = 25


class Employee(Person):

    def __init__(self, name, position):
        super().__init__(name)
        self.position = position
        self.specialization = "Python"


class Client(Person):

    def __init__(self, name):
        super().__init__(name)
        self.ordered = "Website"


employee = Employee("John", "Software developer")
print(employee.name)
print(employee.position)
print()

client = Client("Jim")
print(client.name)
print(client.ordered)
