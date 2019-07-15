import time
import datetime

#time functions
timer = time.time()
time.sleep(2)

elapsed = time.time()-timer

print(elapsed)

timer2 = time.time()
timer3 = time.time()

while True:
    if time.time()-timer > 2:
        print("2 seconds")
        timer = time.time()

    if time.time()-timer2 > 1:
        print("1 second")
        timer2 = time.time()

    if time.time()-timer3 >10:
        break

#date functions

now = datetime.datetime.now();
print(str(now.hour)+":"+str(now.minute))
print(now.strftime("%H:%M %d.%m.%Y")) #24hours clock
print(now.strftime("%I:%M %p %d.%m.%Y")) #12hours clock
print(now.strftime("%I:%M %p %d %b %Y")) #12hours clock
print(now.strftime("%I:%M %p %d %B %Y")) #12hours clock