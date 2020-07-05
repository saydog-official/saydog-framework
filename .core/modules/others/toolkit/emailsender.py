# -*- coding: utf-8 -*-
# coding=utf-8
import os,sys
from time import *
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
                print (g+" EMAIL SENDER"+w+" - by @saydog.official")
                print (w+"---------------------------------------------")
                print (w+"You must login using Google Account first")
                print (w+"because this methods using SMTPLIB")
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
                print (b+"[+]"+w+" Trying to login as:- "+usr)
                msg = MIMEMultipart()
                msg['From'] = usr
                msg['To'] = usr
                msg['Subject'] = "SAYDOG-FRAMEWORK"
                body = "successfully login at e-mail sender"
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
                print ("-------------------------------------------------")
                targ = str(input(w+" To   "+w+": "))
                fake = str(input(w+" From "+w+": "))
                subj = str(input(w+" Sub  "+w+": "))
                mssg = str(input(w+" Mssg "+w+": "))
                print ("-------------------------------------------------")
                print ("")
                ask = str(input("Do you want to insert attachment? (y/n) "))
                print ("")
                if ask == "y" or ask == "Y":
                        try:
                                attch = str(input(b+"[+]"+w+" Path to files    "+w+": "))
                                fname = str(input(b+"[+]"+w+" Confirm filename "+w+": "))
                                print ("")
                                msg = MIMEMultipart()
                                msg['From'] = fake+"<"+usr+">"
                                msg['To'] = targ
                                msg['Subject'] = subj
                                body = mssg
                                msg.attach(MIMEText(body, 'plain'))
                                filename = fname
                                attachment = open(attch,"rb")
                                part = MIMEBase('application', 'octet-stream')
                                part.set_payload((attachment).read())
                                encoders.encode_base64(part)
                                part.add_header('Content-Disposition', "attachment; filename=  %s" % filename)
                                msg.attach(part)
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.starttls()
                                server.login(usr, pwd)
                                text = msg.as_string()
                                server.sendmail(fake, targ, text)
                                server.quit()
                                print ("")
                                print (b+"[+]"+w+" Try to connect to the server SMTP")
                                print (b+"[+]"+w+" Try sending an e-mail")
                                print (b+"[+]"+w+" E-mail has been sent")
                                print ("")
                                x = str(input("["+g+" enter "+w+"]"))
                                if x == " ":
                                        sys.exit(0)
                                else:
                                        sys.exit(0)
                        except FileNotFoundError:
                                print (r+"[!] file not found error")
                                print ("")
                                menu()
                else:
                        msg = MIMEMultipart()
                        msg['From'] = fake+"<"+usr+">"
                        msg['To'] = targ
                        msg['Subject'] = subj
                        body = mssg
                        msg.attach(MIMEText(body, 'plain'))
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(usr, pwd)
                        text = msg.as_string()
                        server.sendmail(fake, targ, text)
                        server.quit()
                        print (b+"[+]"+w+" Try to connect to the server SMTP")
                        print (b+"[+]"+w+" Try sending an e-mail")
                        print (b+"[+]"+w+" E-mail has been sent")
                        print (w)
                        x = str(input("[ enter ]"))
                        if x == " ":
                                sys.exit(0)
                        else:
                                sys.exit(0)

if "__main__" == __name__:
    if "--emailsender-run" in sys.argv:
        menu()
    else:
            os.system("saydog")