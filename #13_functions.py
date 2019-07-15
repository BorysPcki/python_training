
def printme(liczba):
    print("Test: ", end='')
    print(liczba)
printme(5)
printme(10)

def multiply(a,b):
    return a*b

result = multiply(5,6)
print(result)

def divide(a,b=2):
    return a/b

result = divide(b=4,a=2)
print (result)
result = divide(7)
print(result)