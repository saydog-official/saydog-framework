#################### import modules ####################
import os
import sys
import time
import requests
import yagmail
import uncompyle6
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
#################### sprint ####################
def sprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.3 / 100)
#################### main menu ####################
def display():
        try:
                import py_compile
                import socket
                from datetime import datetime
                os.system("clear")
                f = open("main/ip.txt","r")
                logo1 = """
                   ___            _,.---,---.,_
                    |         ,;~'             '~;,
                    |       ,;                     ;,
        <software   |      ;                         ; 
          exploit/> |     ,'                          '
                    |    ,;                           ;,
                    |    ; ;      .           .      ; ;
                    |__  | ;   ______       ______   ; |
                  ___    |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
                   |      |   |        }:{        |   |
     <bruteforce   |      |   l       / | \       !   |
         attack/>  |      .~  (__,.--" .^. "--.,__)  ~.
                   |      |    ----;' / | \ `;----    |
                   |__     \__.       \/^\/       .__/
                     ___    V| \                 / |V
                      |      | |T~\___!___!___/~T| |
                      |      | |'IIII_I_I_I_IIII'| |
        <information  |      |  \,III I I I III,/  |
          gathering/> |       \   `~~~~~~~~~~'    /
                      |         \   .       .   /
                      |__         \.         ./
                                    ^._.^._.^
"""
                logo2 = r+"""
           ...                         ..                   
       .x888888hx    :   ..          dF                     
      d88888888888hxx   @L          '88bu.                  
     8" ... `"*8888%`  9888i   .dL  '*88888bu        uL     
    !  "   ` .xnxx.    `Y888k:*888.   ^"*8888N   .ue888Nc.. 
    X X   .H8888888%:    888E  888I  beWE "888L d88E`"888E` 
    X 'hn8888888*"   >   888E  888I  888E  888E 888E  888E  
    X: `*88888 """+w+"""T h e   H a c k i n g   T o o l k i t"""+w+r+"""  888E
    '8h.. ``     ..x8>   888E  888I  888E  888F 888E  888E  
     `88888888888888f   x888N><888' .888N..888  888& .888E  
      '%8888888888*"     "88"  888   `"888*""   *888" 888&  
         ^"****""`             88F      ""       `"   "888E 
                              98"               .dWi   `88E 
                            ./"                 4888~  J8%  
                           ~`                    ^"===*"` """+w
                logo3 = """
                                    ,--.
 ------------------                {    }
< Saydog Framework >               /   /
 ------------------               /  ~X`
          \                  ,   /   /
           \                {_'-/.__/
            \                 `/-.__L._
             \                /  ' /`\_}
              \              /  ' /
                     ____   /  ' /
              ,-'~~~~    ~~/  ' /_
            ,'             ``~~~  ',
           (                        Y
          {                         I
         {      -                    `,
         |       ',                   )
         |        |   ,..__      __. Y
         |    .,_./  Y ' / ^Y   J   )|
         \           |' /   |   |   ||
          \          L_/    . _ (_,.'(
           \,   ,      ^^""' / |      )
             \_  \          /,L]     /
               /-_~-,       ` `   ./`
              /  '`/{_            )
              \ ' /   ^^\..___,.--`
               \ /
                `
"""
                logo = [logo1,logo2,logo3]
                logo = random.choice(logo)
                print (logo)
                print ("\033[41m  \033[00m Welcome to the:-"+g+" saydog framework version 1.4.0"+w)
                print ("\033[44m  \033[00m This is you're public address:-"+p,f.readline().strip()+w)
                print ("\033[45m  \033[00m Starting console at:-",datetime.today().strftime('%d-%m-%Y Time:- %H:%M:%S'))
                print ("")
                main()
        except KeyboardInterrupt:
                print (r+"[!EXITING]"+w+" The user forces it to stop")
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
#################### menu ####################
def menu():
        while True:
                try:
                        print ("")
                        print (w+"{"+B+W+" MAIN MENU "+w+"}")
                        print ("")
                        print (w+"{"+p+"01"+w+"} Android malicious generator")
                        print (w+"{"+p+"02"+w+"} Metasploit payload generator")
                        print (w+"{"+p+"03"+w+"} Malware infected generator")
                        print (w+"{"+p+"04"+w+"} Information gathering")
                        print (w+"{"+p+"05"+w+"} Social media attack ")
                        print (w+"{"+p+"06"+w+"} Others")
                        print (w+"{"+p+"00"+w+"} Back")
                        print ("")
                        mainmenu()
                except KeyboardInterrupt:
                        print (r+"[!EXITING]"+w+" The user forces it to stop")
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
#################### main menu ####################
def mainmenu():
        dog = str(input(r+"saydog"+w+":"+p+"/menu/"+w+"> "))
        if dog == "0" or dog == "00" or dog == "back":
                display()
        elif dog == "1" or dog == "01":
                os.system("cd modules/malicious/;python android.py --run")
        elif dog == "2" or dog == "02":
                os.system("cd modules/metasploit/;python payload.py --run")
        elif dog == "3" or dog == "03":
                os.system("cd modules/malicious/;python malware.py --run")
        elif dog == "4" or dog == "04":
                os.system("cd modules/infoga/;python infoga.py --run")
        elif dog == "5" or dog == "05":
                os.system("cd modules/socialmedia/bruteforce/;python bruteforce.py --run")
        elif dog == "6" or dog == "06":
                os.system("cd modules/others/;python toolkit.py --run")
        else:
                mainmenu()

#################### main ####################
def main():
        dog = str(input(r+"saydog"+w+" > "))
        if dog == "exit" or dog == "0":
                print (r+"[!EXITING]"+w+" The user forces it to stop")
                sys.exit(0)
        elif dog  == "clear" or dog == "Clear":
                print (b+"[*]"+w+" Exec:- clear")
                os.system("sleep 0.5;clear")
                main()
        elif dog == "banner" or dog == "Banner":
                display()
        elif dog == "help" or dog == "Help" or dog == "?":
                print (w)
                print (w+"{"+B+W+" HELP MENU "+w+"}")
                print (w)
                print (g+" LIST COMMANDS                DESCRIPTIONS"+w)
                print ("-----------------------------------------------------")
                print (w+" help                         show help menu")
                print (w+" banner                       change display logo")
                print (w+" update                       check available update")
                print (w+" report                       report about this tool")
                print (w+" show                         show main menu")
                print (w+" clear                        clear windows")
                print (w+" exit                         exit in this tool")
                print ("-----------------------------------------------------")
                print (w)
                main()
        elif dog == "show" or dog == "Show":
                menu()
                main()
        elif dog == "update":
                print ("")
                os.system("saydog update")
                print ("")
                sys.exit(1)
        elif dog == "report":
                os.system("xdg-open https://github.com/saydog-official/saydog-framework/issues")
                main()
        else:
                main()
###################### main argv ####################
if "__main__" == __name__:
        if "--run" in sys.argv:
            try:
                with open("main/ip.txt") as f:
                    os.system("curl -s ifconfig.co > main/ip.txt")
                    if "<!DOCTYPE" in f.read():
                        print(r+"[*]"+w+" Weak internet connection, please try again")
                    else:
                        os.system("espeak -s140 -ven+18 -z 'Welcome to the saydog framework console, for more information about this tool just type help'")
                        display()
            except KeyboardInterrupt:
                sys.exit(1)
        else:
                sys.exit(1)