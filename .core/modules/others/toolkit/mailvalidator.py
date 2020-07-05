import smtplib, sys, os

def getHost(emailAddress):
	try:
		return emailAddress.split("@")[1]
	except Exception as exc:
		print "'" + emailAddress + "' is not a valid email address"
		sys.exit(1)
		return -1	

def resolveMX(emailHost):
	global hostItems
	hostDict={}
	try:
		records = dns.resolver.query(emailHost, "MX")
	except Exception as exc:
		print "Could not extract records from host."
		sys.exit(1)
		return -1
	for r in records:
		hostDict[r.exchange] = r.preference
	hostItems = hostDict.items()
	hostItems.sort()

def checkEmail(emailAddress):
	result = True
	smtp = smtplib.SMTP()
	for x in hostItems:
		try:
			host = x[0][:-1]
			host = ".".join(host)
			connectLog = smtp.connect(host)
			heloLog = smtp.helo("google.com")
			output(connectLog)
			output(heloLog)
		except Exception as exc:
			errorString = "Could not connect to Server: " + host
			errorString += "\nTrying next record (if any)"
			output(errorString)
			sys.exit(1)	
			continue
		else:
			result = False
			break
	if result:
		print "Could not resolve any hosts for: " + emailAddress
		return -1
	try:
		sendLog = smtp.sendmail("test@google.com",emailAddress,"IgnoreMessage")
		output(sendLog)
	except Exception as exc:
		print "Email is not valid."
		sys.exit(1)
	else:
		print "Email: " + emailAddress + " is valid!"
		validList.append(emailAddress)

#Print more output if verbose argument is given
def output(string):
	if verbose:
		print string

#Print the documentation
def printHelp():
	print ""
	print "Verify if email addresses are valid by checking SMTP server\n"
	
	print "Usage:\n\tpython verify-email.py -e <email> -v\n"
	print "Arguments:\n"
	print " -h or --help","This help".rjust(28)
	print " -v or --verbose","Increases verbosity".rjust(35)
	print " -e or --email <email>","Specify one email address to check".rjust(44)
	print " -f or --file <file>","Specify a file of emails delimeted by line".rjust(54)
	print "\nExample:\n\tpython verify-email.py -e admin@example.org -v"
	print "\tpython verify-email.py --file email.txt\n"
	quit()

verbose=False
suppliedInput = 0
validList = []

if not (len(sys.argv) == 3 or len(sys.argv) == 4):
	printHelp()
for i in range(1,len(sys.argv)):
	if sys.argv[i] == "-h" or sys.argv[i] == "--help":
		printHelp()
	elif sys.argv[i] == "-v" or sys.argv[i] == "--verbose":
		verbose=True
		continue
	elif sys.argv[i] == "-e" or sys.argv[i] == "--email":
		if suppliedInput == 0:
			inputEmail = sys.argv[i+1]
			suppliedInput = 1
		else:
			printHelp()
	elif sys.argv[i] == "-f" or sys.argv[i] == "--file":
		if suppliedInput == 0:
			inputFile = sys.argv[i+1]
			suppliedInput = 2
		else:
			printHelp()
try:
	if suppliedInput == 0:
		printHelp()
	elif suppliedInput == 1:
		host = getHost(inputEmail)
		if not host == -1:
			if not resolveMX(host) == -1:
				checkEmail(inputEmail)
	elif suppliedInput == 2:
		try:
			file = open(inputFile,"r")
		except Exception as exc:
			print "Could not open '" + inputFile + "' for reading"
			sys.exit(1)
			quit()
		else:
			for email in file:
				email = email.replace("\n","")
				print "Checking: " + email
				host = getHost(email)	
				if host == -1:
					continue
				elif resolveMX(host) == -1:
					continue
				elif checkEmail(email) == -1:
					continue
except KeyboardInterrupt:
	print "Keyboard Interrupt Detected."

if validList:
	print "\nValid Emails: \n=========="
	for item in validList:
		print item
	print ""
