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
        try:
                print ("")
                print (w+"{"+B+W+" OTHERS "+w+"}")
                print ("")
                print (w+"{"+p+"01"+w+"} Email sender")
                print (w+"{"+p+"02"+w+"} Python logger generator")
                print (w+"{"+p+"03"+w+"} Python minicrypto locker")
                print (w+"{"+p+"04"+w+"} Python terabyte attack")
                print (w+"{"+p+"05"+w+"} ZIP Password bruteforce")
                print (w+"{"+p+"06"+w+"} IP to geolocate")
                print (w+"{"+p+"07"+w+"} Bulk mail checker")
                print ("")
                print (w+"{"+p+"00"+w+"} Back to main menu")
                print ("")
                main()
        except KeyboardInterrupt:
                sys.exit(1)

#################### main ####################
def main():
        dog = str(input(r+"saydog"+w+":"+p+"/others/"+w+"> "))
        if dog == "back" or dog == "0" or dog == "00":
                sys.exit(1)
        elif dog == "1" or dog == "01":
                os.system("cd toolkit;python emailsender.py --emailsender-run")
        elif dog == "2" or dog == "02":
                os.system("cd toolkit;python genlogger.py --genlogger-run")
        elif dog == "3" or dog == "03":
                os.system("cd toolkit;python minicrypto.py --minicrypto-run")
        elif dog == "4" or dog == "04":
                os.system("cd toolkit;python terabyte.py --terabyte-run")
        elif dog == "5" or dog == "05":
                os.system("cd toolkit;python brutezip.py")
        elif dog == "6" or dog == "06":
                os.system("cd toolkit;python2 iploctrack.py")
        elif dog == "7" or dog == "07":
                try:
                        print (w)
                        checkfile = str(input(b+"[+]"+w+" File to check [combo.txt]: "))
                        print (b+"[+]"+w+" Mail checker is running")
                        print (b+"[+]"+w+" This could take a while, please wait")
                        os.system("cd toolkit/mailchecker;python2 crack.py "+checkfile+" 400 0 &> /dev//null")
                        print (b+"[+]"+w+" Mail checker stopped")
                        print (b+"[+]"+w+" Result saved as:- "+g+"result/mailchecker_result.txt"+w)
                        print (w)
                        dog = str(input("[ enter ]"))
                except KeyboardInterrupt:
                        sys.exit(1)
                except IndexError:
                        sys.exit(1)
        else:
                main()

if "__main__" == __name__:
    if "--run" in sys.argv:
        menu()
    else:
            os.system("saydog")
