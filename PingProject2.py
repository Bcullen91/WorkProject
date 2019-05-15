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

waittime= int(0)
running= str("yes")
while running == "yes":
    while waittime > 0:
        print(waittime)
        time.sleep(1)
        waittime = waittime - 1
        continue
    while waittime == 0:
        while ping("192.168.5.139") == True:
            print("iPhone is Online")
            time.sleep(1)
        else:
            print("iPhone is now Offline")
            waittime= waittime + 3
            print("Looping")
            break
    continue
else:
    print("Some error occurred and the script is not running")
