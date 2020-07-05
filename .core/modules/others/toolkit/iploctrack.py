# -*- coding: utf-8 -*- 
import os,sys,time
import json
import requests
import re

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
	try:
		print ("")
		target = raw_input(b+'[+]'+w+' Enter an ip address: ') #User Input
		send_url = 'http://ip-api.com/json/'+target #Finds Targets
		r = requests.get(send_url)
		j = json.loads(r.text)
		cn = j['country']
		cc = j['countryCode']
		rg = j['region']
		rn = j['regionName']
		ct = j['city']
		lo = j['lon']
		la = j['lat']
		tz = j['timezone']
		sp = j['isp']
		rg = j['org']
		ss = j['as']
		print ("")
		print (g+"LOCATION FOUNDED "+w+"- by @saydog.official")
		print ("-------------------------------------------")
		print (w+"The current location founded using IP public")
		print ("-------------------------------------------")
		print ("COUNTRY : "+str(cn))
		print ("CITY    : "+str(ct))
		print ("TIMEZONE: "+str(ct))
		print ("G-MAPS  : https://google.com/maps?q="+str(la)+","+str(lo))
		print ("ISP     : "+str(sp))
		print ("-------------------------------------------")
		print ("")
		dog = raw_input("[ enter ]")
		if dog == "":
		        sys.exit(1)
		else:
		        sys.exit(1)
	except (ValueError,KeyError):
		print ("")
		print ("\033[31;1m[!ERROR]"+w+" Invalid ip address, please try again")
		print ("")
	except KeyboardInterrupt:
		sys.exit(1)

main()