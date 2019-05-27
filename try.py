import subprocess
import re
import time
import logging

dater = time.strftime("%Y%m%d")
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='./derp/'+ dater + 'DERP-LOG.log',
                    filemode='a')
logDerp = logging.getLogger('theLog')
timestr2 = time.strftime("%Y-%m-%d")
logDerp.info("Testing")

hostname = "google.com"

pingResponse = subprocess.Popen(
    ["ping", hostname, "-n", '5'], stdout=subprocess.PIPE).stdout.read()
pingResponse = pingResponse.decode()

outs = re.findall(r'time=(\d+)', pingResponse)
pingErs = re.findall(r'.*request could not.com', pingResponse)
for out in outs:
    logDerp.info("time="+out+"ms")
for pingEr in pingErs:
    logDerp.error("Error: "+ pingEr)

#print("Output is: " + re.findall(r'time=(\d+)', pingResponse))
print("Ping response: \n" + pingResponse)