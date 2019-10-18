try:
    file = open("test.txt", "w+")
    file.write("Hello")
    file.read("5")
    file.close()
except FileNotFoundError as e:
    print(str(e) + " - " + "create file!")
except TypeError as e:
    print(str(e)+ " - " + "insert integer in read function!")
except Exception as e:
    print("Error occurred: " + str(e))

print("OK")

