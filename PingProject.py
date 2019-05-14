import os

# DL Adding my own IP - because this is my code
dlHostName = "192.168.1.213"
# hostname = "192.168.5.139"
#change to any ip on your network, im using my iphones ip.
# you might have to change the -c to -n for windows
# response = os.system("ping -n 10 " + hostname)
dlResponse = os.system("ping -n 10 " + dlHostName)

#and then check the response...
# if response == 0:
#     print(hostname, 'is up!')
# else:
#     print(hostname, 'is down!')


if dlResponse == 0:
    print(dlHostName, 'is up!')
else:
    print(dlHostName, 'is down!')


    #Yes, I commented out your code - deal with it