#################### import modules ####################
import os
import sys
import time
import requests
import random
#################### fonts colors ####################
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
#################### main menu ####################
def menu():
        while True:
                try:
                        print ("")
                        print (w+"{"+B+W+" METASPLOIT PAYLOAD "+w+"}")
                        print ("")
                        print (w+"{"+p+"01"+w+"} Android payload generator")
                        print (w+"{"+p+"02"+w+"} Apple ios payload generator")
                        print (w+"{"+p+"03"+w+"} Windows payload generator")
                        print (w+"{"+p+"04"+w+"} Web payload generator")
                        print (w+"{"+p+"05"+w+"} Scripting payload generator")
                        print ("")
                        print (w+"{"+p+"00"+w+"} Back to main menu")
                        print ("")
                        dog = str(input(r+"saydog"+w+":"+p+"/payload/"+w+"> "))
                        if dog == "0" or dog == "back":
                                sys.exit(1)
                        elif dog == "1" or dog == "01":
                                os.system("cd android/;python android.py --run")
                        elif dog == "2" or dog == "02":
                                os.system("cd iphone/;python iphone.py --run")
                        elif dog == "3" or dog == "03":
                                os.system("cd windows/;python windows.py --run")
                        elif dog == "4" or dog == "04":
                                os.system("cd website/;python website.py --run")
                        elif dog == "5" or dog == "05":
                                os.system("cd cmd_unix/;python cmd_unix.py --run")
                        else:
                                menu()
                except KeyboardInterrupt:
                        sys.exit(1)
                except ModuleNotFoundError:
                        sys.exit(1)
                except NameError:
                        sys.exit(1)
                except EOFError:
                        sys.exit(1)
                except FileNotFoundError:
                        sys.exit(1)
###################### main argv ####################
if "__main__" == __name__:
        if "--run" in sys.argv:
                menu()
        else:
                os.system("saydog")