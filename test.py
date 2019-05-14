import socket
# This Python libary and code was written for Python 2 (Which is outdated). Here is some info on the Python 3 version: https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
from urllib2 import urlopen, URLError, HTTPError


socket.setdefaulttimeout( 23 )  # timeout in seconds

url = 'http://google.com/'
try :
    response = urlopen( url )
    
# Using " , [variable] is an out-dated method. With python 3 - you need to use the word "as" in place of ","    
except HTTPError as e:
    # Adding '(' and ')' to print() function
    # Also adding inverted commas
    print("The server couldnt fulfill the request. Reason:", str(e.code))
except URLError as e:
    print ("We failed to reach a server. Reason:", str(e.reason))
else :
    html = response.read()
    print("got response!")
        # do something, turn the light on/off or whatever
