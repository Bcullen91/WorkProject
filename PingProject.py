import time

waitime= int(5)
while waitime > 0:
    print(waitime)
    waitime= waitime - 1
    time.sleep(1)
else:
    print("Waittime is 0 now")

