import os,sys,time,fileinput
def rename():
	cek = open("~/../usr/bin/apktool241").read()
	if "jarfile=apktool.jar" in cek:
		pass
	else:
		sys.exit(1)
	replaces = {"jarfile=apktool.jar":"jarfile=apktool241.jar"}
	for line in fileinput.input("~/../usr/bin/apktool241", inplace=True):
		for search in replaces:
			replaced = replaces[search]
			line = line.replace(search,replaced)
		print(line, end="")
		pass
	sys.exit(1)

rename()
