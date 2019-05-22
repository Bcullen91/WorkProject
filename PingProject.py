import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import time
print("This is working")
reboottime = 10

for i in range(reboottime, 0, -1):
    print("Your device will be powered on in " + str(i) + " seconds")
    time.sleep(1)

print("Finished")