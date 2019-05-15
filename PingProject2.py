import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import time

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

waittime= int(0)  # Sets waittime to 0 so it will immediately start running
running= str("yes")  # Sets the variable running to yes so it will always run constantly
while running == "yes":  # Starts the infinite loops since running will never not be "yes"
    while waittime > 0:  # If waittime is greater than 0 it prints the waitime and then waits 1 second
        print(waittime)
        time.sleep(1)
        waittime = waittime - 1
        continue
    while waittime == 0:  # If waittime is 0 it will run the ping command. 
        while ping("192.168.5.139") == True:  # if the ping is successful it will return True
            print("iPhone is Online")
            time.sleep(1)
        else:  #If the ping fails it will add to the waittime and then loop to ping again
            print("iPhone is now Offline")
            waittime= waittime + 3
            print("Looping")
            break
    continue
else:
    print("Some error occurred and the script is not running")
