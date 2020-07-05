import os,sys
import time
import re
from api import apiweb
try:
        import requests
except ModuleNotFoundError:
        os.system("pythom3 -m pip install requests")

u='\033[4m'
w="\033[00m"
r="\033[91;1m"
b="\033[34;1m"
y="\033[33;1m"
g="\033[32;1m"

def menu():
        print ("")
        target = str(input(b+"[+]"+w+" Domain target: "))
        print (b+"[+]"+w+" Trying to find host DNS for "+target)
        time.sleep(5)
        x = apiweb.apiweb(5, target)
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