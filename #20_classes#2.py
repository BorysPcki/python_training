class Calculator():

    def __init__(self):
        self.last_result = 0

    def add(self, a, b):
        result = a + b
        self.last_result = result
        print(result)

    def substract(self, a, b):
        result = a - b
        self.last_result = result
        print(result)


calc = Calculator()
calc.add(5, 3)
calc.substract(12, 15)

calc2 = Calculator()
calc2.add(50, 50)
calc2.add(21, 37)

print("Last result calc: {}".format(calc.last_result))
print("Last result calc2: {}".format(calc2.last_result))
