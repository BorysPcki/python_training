import os
import shutil
from time import sleep

list1 = os.listdir(".")
print(list1)

list2 = os.listdir("C:/Windows")
print(list2)

for item in os.listdir("."):
    if os.path.isfile(item):
        print("{} is file".format(item))

os.mkdir("new_folder")
sleep(2)
os.rename("new_folder", "renamed_folder")
sleep(2)
os.rmdir("renamed_folder")

open("test.txt", "w").close()
sleep(2)
os.remove("test.txt")

path = "files/01/data.txt"
os.makedirs(os.path.dirname(path))
open("path", "w").close()
sleep(2)
shutil.rmtree("files")
