import os
import sys
import time
import zipfile
try:
        from tqdm import tqdm
except ModuleNotFoundError:
        os.system("python3 -m pip install tqdm &> /dev//null")
#################### font colors ####################
w="\033[00m"
r="\033[31;1m"
g="\033[32;1m"
y="\033[33;1m"
d="\033[2;31m"
b="\033[34;1m"
p="\033[35;1m"
c="\033[36;1m"
W="\033[47m"
R="\033[41m"
B="\033[30m"
G="\033[90m"
BG="\033[100m"
#################### main ####################

def main():
        os.system("mkdir zip/;cd zip/")
        print(w)
        zip_file=str(input(b+"[+]"+w+" zip file path (ex: /sdcard/file.zip): "))
        if zip_file == "" or zip_file == " ":
                print ("")
                print (r+"[!ERROR]"+w+" file not found")
                print ("")
                sys.exit(1)
        else:
                pass
        wordlist=str(input(b+"[+]"+w+" wordlist path (ex:  /sdcard/pass.txt): "))
        if wordlist == "" or wordlist == " ":
                print ("")
                print (r+"[!ERROR]"+w+" file not found")
                print ("")
                os.system("rm -rf zip/")
                sys.exit(1)
        else:
                pass
        zip_file = zipfile.ZipFile(zip_file)
        n_words = len(list(open(wordlist, "rb")))
        print(w)
        print(b+"[+]"+w+" List of password for cracking:", n_words)
        print(b+"[+]"+w+" Bruteforce is started")
        print(w)
        with open(wordlist, "rb") as wordlist:
                for word in wordlist:
                        try:
                            zip_file.extractall(pwd=word.strip())
                        except:
                            continue
                        else:
                            print(w+"["+g+"!PASSWORD FOUND"+w+"]"+w+" the password is:-"+y, word.decode().strip())
                            print(w)
                            dog = str(input(w+"[ enter "+w+"]"))
                            os.system("rm -rf zip/")
                            if dog == " ":
                                sys.exit(0)
                            else:
                                sys.exit(0)
        print(r+"[!]"+w+" Password not found, please try again later")
        print(w)

#################### menu ####################
def menu():
        try:
                main()
        except KeyboardInterrupt:
                os.system("rm -rf zip/")
                sys.exit(1)
        except FileNotFoundError:
                print(r+"[!ERROR] "+w+"File not found")
                sys.exit(1)

menu()