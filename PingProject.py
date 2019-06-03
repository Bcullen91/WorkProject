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
timestr = time.strftime("%Y%m%d")
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='./logs/'+ timestr +'-LOG.log',
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
timestr2 = time.strftime("%Y-%m-%d")

host = str("8.8.8.8")
logger1.debug("LOG STARTED: "+ timestr2)
logger1.info("TARGET ASSIGNED AS: " + host)


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
    while offTime > 3:
        print(" Your device is rebooting")
        logger1.info("INITIALIZE REBOOT")
        reboot()
        time.sleep(1)
        sincereboot = 3
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
            timestr3 = time.strftime("%H:%M:%S")
            logger1.info("TARGET (SUCCESS): " + host + " At " + timestr3)
            print(" Connection is Online")
            waittime= 3
            offTime= 0
            break
        else:           
            logger1.error("TARGET (FAILED): " + host)
            print(" Connection is now Offline")
            offTime= offTime + 7
            print(" The Connection has been offline for: ",end="")
            print(str(offTime) + " seconds",end='\r', flush=True)
            logger1.error("CONNECTION DOWN FOR: " + str(offTime) + " SECONDS")
            break
    continue
else:
    logger1.error("PROGRAM FAILED")
    print(" Some error occurred and the the 'yes' loop failed.")
