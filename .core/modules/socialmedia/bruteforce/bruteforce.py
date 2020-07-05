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
                        print (w+"{"+B+W+" SOCIAL BRUTEFORCE "+w+"}")
                        print ("")
                        print (w+"{"+p+"01"+w+"} Instagram bruteforce")
                        print (w+"{"+p+"02"+w+"} Facebook bruteforce")
                        print (w+"{"+p+"03"+w+"} Gmail bruteforce")
                        print (w+"{"+p+"04"+w+"} Wordlist generator")
                        print (w+"{"+p+"05"+w+"} Edit default proxylist")
                        print ("")
                        print (w+"{"+p+"00"+w+"} Back to main menu")
                        print ("")
                        main()
                except KeyboardInterrupt:
                        sys.exit(1)
                except ModuleNotFoundError:
                        print (r+"[!ERROR]"+w+" Module not found!")
                        sys.exit(1)
                except NameError:
                        sys.exit(1)
                except EOFError:
                        sys.exit(1)
                except FileNotFoundError:
                        print (r+"[!ERROR]"+w+" File not found!")
                        sys.exit(1)
#################### main ####################
def main():
        dog = str(input(r+"saydog"+w+":"+p+"/bruteforce/"+w+"> "))
        if dog == "back" or dog == "0" or dog == "00":
                sys.exit(1)
        elif dog == "1" or dog == "01":
                os.system("tor &> /dev/null &")
                print ("")
                user = str(input(b+"[+]"+w+" Username target: "))
                if user == "" or user == " ":
                        print ("")
                        print (r+"[!ERROR]"+w+" username not found!")
                        print ("")
                        sys.exit(1)
                else:
                        user = user
                        pass
                wordlist = str(input(b+"[+]"+w+" Wordlist path: "))
                if wordlist == "" or wordlist == " ":
                        print ("")
                        print (r+"[!ERROR]"+w+" wordlist not found!")
                        print ("")
                        sys.exit(1)
                else:
                        wordlist = wordlist
                        pass
                print ("")
                os.system('python instagram.py -u '+user+' -w '+wordlist+' -p proxys.txt -d -v')
        elif dog == "2" or dog == "02":
                os.system("python2 facebook.py --facebook-run")
        elif dog == "3" or dog == "03":
                os.system("python gmail.py")
        elif dog == "4" or dog == "04":
                os.system("python wordlist.py --wordlist-run")
        elif dog == "5" or dog == "05":
                os.system("nano proxys.txt")
                print (w)
                print (b+"[+]"+w+" Default proxylist updated")
                print (w)
                dog = str(input("[ enter ]"))
                if dog == "":
                        menu()
                else:
                        menu()
        else:
                main()

if "__main__" == __name__:
    if "--run" in sys.argv:
        menu()
    else:
            os.system("saydog")