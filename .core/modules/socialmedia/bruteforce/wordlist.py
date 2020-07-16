import os, sys
import time

W="\033[00m"
B="\033[34m"
a=""
b=""
c=""
d=""
e=""
f=""
g=""
h=""
i=""
j=""
k=""
l=""

def main():
        try:
                global a,b,c,d,e,f,g,h,i,j,k,l
                print (W)
                print("\033[32;1mWORDLIST GENERATOR\033[00m - by @saydog.official")
                print("---------------------------------------")
                print("Wordlist generator for bruteforce attack")
                print("one wordlist for all socialmedia bruteforce")
                print("---------------------------------------")
                print("")
                print("\033[32;1mALPHABET ONLY\033[00m")
                print("")
                a = input("firstname     : ")
                b = input("middlename    : ")
                c = input("lastname      : ")
                d = input("nickname      : ")
                print("")
                print("---------------------------------------")
                print("")
                print("\033[32;1mNUMERIC ONLY\033[00m")
                print("")
                e = (str(input("date of birth : ")))
                f = (str(input("month of birth: ")))
                g = (str(input("year or birth : ")))
                print("")
                print("---------------------------------------")
                print("")
                print(B+"[+]"+W+" Wordlist has been genrrated")
                h = "@"
                i = "_"
                j = "123"
                k = "1234"
                l = "12345"
                word = (a+e,a+f,a+g,a+e+f,a+e+f+g,a+g+f+e,b+e,b+f,b+g,b+e+f,b+e+f+g,b+g+f+e,c+e,c+f,c+g,c+e+f,c+e+f+g,c+g+f+e,d+e,d+f,d+g,d+e+f,d+e+f+g,d+g+f+e,a+b+e,a+b+f,a+b+g,a+b+e+f,a+b+e+f+g,a+b+g+f+e,b+c+e,b+c+f,b+c+g,b+c+e+f,b+c+e+f+g,b+c+g+f+e,c+d+e,c+d+f,c+d+g,c+d+e+f,c+d+e+f+g,c+d+g+f+e,b+d+e,b+d+f,b+d+g,b+d+e+f,b+d+e+f+g,b+d+g+f+e,a+d+e,a+d+f,a+d+g,a+d+e+f,a+d+e+f+g,a+d+g+f+e,h+a+e,h+a+f,h+a+g,h+a+e+f,h+a+e+f+g,h+a+g+f+e,h+b+e,h+b+f,h+b+g,h+b+e+f,h+b+e+f+g,h+b+g+f+e,h+c+e,h+c+f,h+c+g,h+c+e+f,h+c+e+f+g,h+c+g+f+e,h+d+e,h+d+f,h+d+g,h+d+e+f,h+d+e+f+g,h+d+g+f+e,i+a+e,i+a+f,i+a+g,i+a+e+f,i+a+e+f+g,i+a+g+f+e,i+b+e,i+b+f,i+b+g,i+b+e+f,i+b+e+f+g,i+b+g+f+e,i+c+e,i+c+f,i+c+g,i+c+e+f,i+c+e+f+g,i+c+g+f+e,i+d+e,i+d+f,i+d+g,i+d+e+f,i+d+e+f+g,i+d+g+f+e,a+j,a+b+j,a+b+c+j,a+b+c+d+j,b+j,b+c+j,b+c+d+j,c+d+j,d+a+j,d+b+j,d+c+j,d+b+a+j,d+b+c+j,a+k,a+b+k,a+b+c+k,a+b+c+d+k,b+k,b+c+k,b+c+d+k,c+d+k,d+a+k,d+b+k,d+c+k,d+b+a+k,d+b+c+k,a+l,a+b+l,a+b+c+l,a+b+c+d+l,b+l,b+c+l,b+c+d+l,c+d+l,d+a+l,d+b+l,d+c+l,d+b+a+l,d+b+c+l) 
                with open("../../../../result/pass.txt", "w+") as filehandle:
                        filehandle.writelines("%s\n" % place for place in word)
                        filehandle.close()
                        sv = str(input(B+"[+]"+W+" save file to (ex: /sdcard): "))
                        os.system("cat ../../../../result/pass.txt > /"+sv+"/pass.txt")
                        print(B+"[+]"+W+" file saved as:- \033[32;1m"+sv+"/pass.txt"+W)
                        print (W)
                        dog = str(input("[ enter ]"))
                        if dog == "":
                                sys.exit(1)
                        else:
                                sys.exit(1)
        except KeyboardInterrupt:
                sys.exit(1)

if "__main__" == __name__:
    if "--wordlist-run" in sys.argv:
        main()
    else:
            os.system("saydog")
