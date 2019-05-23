import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import time
# import RPi.GPIO as GPIO
#Adding Python's standard logger
import logging



sincereboot = int(2)     
offTime= int(0)         
waittime= int(0)         
running= str("yes") 

# GPIO.setwarnings(True)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(12, GPIO.OUT)

#Logger config
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    filename='./myapp.log',
                    filemode='a')
# Creating handler that writes debug messages to sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# Setting simple console format
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# Assign format to handler
console.setFormatter(formatter)
# Adding handler to root logger
logging.getLogger('').addHandler(console)
# Set logger variable
logger1 = logging.getLogger('mainLog')

host = str("8.8.8.8")
logger1.info("Host Assigned: " + host)


def reboot():
    # GPIO.output(12, GPIO.HIGH)
    logger1.info("REBOOT INITIATED")
    for i in range(3, 0, -1):
        print("Your device will be powered on in: ",end="",flush=True)
        print(str(i) + " seconds",end='\r',flush=True)
        time.sleep(1)
    # GPIO.output(12, GPIO.LOW)
    print("Your device has been rebooted and should be powering on now.")

def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0

while running == "yes":     
    while sincereboot > 0:
        print(" Time Since Last Reboot: ",end="")
        print(str(sincereboot),end="\r", flush=True)
        time.sleep(1)
        sincereboot = sincereboot - 1
        continue
    while offTime > 20:
        print(" Your device is rebooting")
        logger1.info("INITIALIZE REBOOT")
        reboot()
        time.sleep(30)
        sincereboot = 20
        print(" Testing after the reboot")
        offTime= 0
        break
    while waittime > 0:          
        print(" Waiting ",end="")
        print(str(waittime),end="\r",flush=True)
        time.sleep(1)
        waittime = waittime - 1
        continue
    while waittime == 0:           
        while ping(host) == True:
            logger1.info("CONNECTION ESTABLISHED")
            print(" Google is Online")
            waittime= 3
            offTime= 0
            break
        else:           
            logger1.error("CONNECTION FAILED")
            print(" Google is now Offline")
            offTime= offTime + 7
            print(" The Google has been offline for: ",end="")
            print(str(offTime) + " seconds",end='\r', flush=True)
            logger1.info("CONNECTION DOWN FOR: " + str(offTime) + " SECONDS")
            break
    continue
else:
    logger1.error("PROGRAM FAILED")
    print(" Some error occurred and the the 'yes' loop failed.")
