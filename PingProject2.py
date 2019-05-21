import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import time
import RPi.GPIO as GPIO

host= str("192.168.5.137")

GPIO.setmode(GPIO.BCM)
# I have the relay plugged into GPIO 2, which is in slot 13. 
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, GPIO.HIGH)

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'
    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0

offTime= int(0)         # Creates a variable that will be how long its been offline
waittime= int(0)         # Sets waittime to 0 so it will immediately start running
running= str("yes")          # Sets the variable running to yes so it will always run constantly
while running == "yes":           # Starts the infinite loops since running will never not be "yes"
    if offTime > 60:
        print("This will eventually be a signal to power off the kit")
        time.sleep(10)          # This will eventually be 480 seconds, which is 8 minutes, 
        offTime= 0
    else:
        pass
    while waittime > 0:          
        print("Waiting " + str(waittime) + " seconds")
        time.sleep(1)
        waittime = waittime - 1
        continue
    while waittime == 0:           
        while ping(host) == True:           
            print("iPhone is Online")
            GPIO.output(2, GPIO.LOW)
            print("Turning on the relay")
            time.sleep(3)
            GPIO.cleanup()
            waittime= 3
            offTime= 0
            break
        else:           
            print("iPhone is now Offline")
            offTime= offTime + 5
            print("The iPhone has been offline for " + str(offTime) + " seconds")
            print("Looping")
            break
    continue
else:
    print("Some error occurred and the script is not running")
