import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import time
import RPi.GPIO as GPIO

host= str("192.168.5.137")   # Change this IP address to whatever you want to test connection to. 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

def reboot():
    GPIO.output(12, GPIO.HIGH)
    for i in range(30,0):
        print("Your device will be powered on in " + i + " seconds")
        time.sleep(1)
    GPIO.output(12, GPIO.LOW)
    sincereboot = 420
    print("Your device has been rebooted and should be powering on now.")


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'
    # Building the command. Ex: "ping -c 1 google.com" [ping, system, number of pings, host ip]
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0

offTime= int(0)         # Creates a variable that will be how long its been offline
waittime= int(0)         # Sets waittime to 0 so it will immediately start running
running= str("yes") 
sincereboot = int(420)     # Sets variable for since reboot so it wont keep power cycling (420 seconds for 7 minutes)

while running == "yes":       # Starts the infinite loops since running will never not be "yes"
    while sincereboot > 0:
        time.sleep(1)
        sincereboot = sincereboot - 1
        continue
    if offTime > 60:
        print("Your device is rebooting")
        reboot()
        time.sleep(10)           
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
            waittime= 3
            offTime= 0
            break
        else:           
            print("iPhone is now Offline")
            offTime= offTime + 5
            print("The iPhone has been offline for " + str(offTime) + " seconds")
            break
    continue
else
    running= str("yes")
    print("Some error occurred and the the 'yes' loop failed.")
