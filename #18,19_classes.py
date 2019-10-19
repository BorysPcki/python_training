class Calculator():

    def __init__(self):
        print("Init")

    def __del__(self):
        print("Del")

    def __str__(self):
        return "__str__"

    def __int__(self):
        return 10

    def __len__(self):
        return 2

    def __bool__(self):
        return True

    def add(self, a, b):
        result = a + b
        print(result)

    def substract(self, a, b):
        result = a - b
        print(result)


def main():
    print("1")
    calc = Calculator()
    print("2")
    calc.add(10, 15)
    print("3")
    print(calc)
    print(int(calc) + 10)
    print(len(calc))

    if calc:
        print("True")
    else:
        print("False")


main()
print("4")
