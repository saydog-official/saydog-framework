import os
import sys
import time
from sys import *

#################### font colors ####################
w="\033[00m"
r="\033[31;1m"
g="\033[32;1m"
y="\033[33m"
d="\033[2;31m"
b="\033[34;1m"
p="\033[35;1m"
c="\033[36;1m"
W="\033[47m"
R="\033[41m"
B="\033[30m"
G="\033[90m"
BG="\033[100m"
#################### menu ####################
def menu():
        while True:
                try:
                        print ("")
                        print (w+"{"+B+W+" INFORMATION GATHERING "+w+"}")
                        print ("")
                        print (w+"{"+p+"01"+w+"} Find admin login")
                        print (w+"{"+p+"02"+w+"} Find host dns")
                        print (w+"{"+p+"03"+w+"} Find shared dns")
                        print (w+"{"+p+"04"+w+"} Dns lookup")
                        print (w+"{"+p+"05"+w+"} Ip location lookup")
                        print (w+"{"+p+"06"+w+"} Sub domain lookup")
                        print (w+"{"+p+"07"+w+"} Reverse ip lookup")
                        print (w+"{"+p+"08"+w+"} Whois lookup")
                        print (w+"{"+p+"09"+w+"} Tcp scanner")
                        print ("")
                        print (w+"{"+p+"00"+w+"} Back to main menu")
                        print ("")
                        main()
                except KeyboardInterrupt:
                        sys.exit(1)

#################### main ####################
def main():
        dog = str(input(r+"saydog"+w+":"+p+"/infoga/"+w+"> "))
        if dog == "back" or dog == "0" or dog == "00":
                sys.exit(1)
        elif dog == "1" or dog == "01":
                os.system("php adminfinder.php")
        elif dog == "2" or dog == "02":
                os.system("python findhostdns.py")
        elif dog == "3" or dog == "03":
                os.system("python findsharedns.py")
        elif dog == "4" or dog == "04":
                os.system("python dnslookup.py")
        elif dog == "5" or dog == "05":
                os.system("python iploclookup.py")
        elif dog == "6" or dog == "06":
                os.system("python sublookup.py")
        elif dog == "7" or dog == "07":
                os.system("python reiplookup.py")
        elif dog == "8" or dog == "08":
                os.system("python whoislookup.py")
        elif dog == "9" or dog == "09":
                os.system("python tcpscan.py")
        else:
                main()

if "__main__" == __name__:
    if "--run" in sys.argv:
        menu()
    else:
            os.system("saydog")