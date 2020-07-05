import os,sys
import time
from api import apiweb
try:
        import requests
        os.system("python3 -m pip install requests &> /dev//null")
except KeyboardInterrupt:
        sys.exit(1)

u="\033[4m"
w="\033[00m"
r="\033[91;1m"
b="\033[34;1m"
y="\033[33;1m"
g="\033[32;1m"

def menu():
        print ("")
        target = str(input(b+"[+]"+w+" Domain target: "))
        print (b+"[+]"+w+" Trying to lookup Subdomain for "+target)
        time.sleep(5)
        x = apiweb.apiweb(12, target)
        print ("")
        print (w+"=================================================")
        print (g,x)
        print (w+"=================================================")
        print ("")
        print (b+"[+]"+w+" Result for:- "+target)
        print ("")
        dog = str(input(w+"[ enter ]"))
        if dog == " ":
                sys.exit(0)
        else:
                sys.exit(0)

menu()