
f = open("file.txt", "a+")
f.write("123 \n")
f.write("abc \n")
f.close()

f = open("file.txt", "r")
print(f.read(7))
print(f.readline())
f.close()

f = open("file.txt", "r")
print(f.readline())
f.close()

f = open("file.txt", "a+")
f.seek(7, 0)
print(f.read(7))
f.close()

f = open("file.txt", "r")
print(f.readlines())
f.close()

f = open("file.txt", "r")
for line in f.readlines():
    print(line.rstrip())
f.close()
