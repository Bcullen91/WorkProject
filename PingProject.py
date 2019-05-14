import os

hostname = "192.168.5.139" #change to any ip on your network, im using my iphones ip.
# you might have to change the -c to -n for windows
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
    print(hostname, 'is up!')
else:
    print(hostname, 'is down!')
