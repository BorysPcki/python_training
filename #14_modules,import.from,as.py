import foo_14
foo_14.test("bar")

from foo_14 import apple
apple("iphone")

from time import sleep
print("a")
sleep(1)
print("b")

from foo_14 import *
test("baar")

def apple(text):
    print("Pineapple: ",end='')
    print(text)

from foo_14 import apple as pineapple
pineapple("uphone")