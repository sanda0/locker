# code by sandakelum priyamantha
import os
import glob
try:
	os.mkdir("log")
except:
	print("log folder is created!")

lslist = glob.glob("log/*.*")
# print(lslist)

if "log/pass.spw" not in lslist:
	p = open("log/pass.spw","w")
	p.close()
else:
	print("file is created!")

def setpass(pass1,pass2):
	p = open("log/pass.spw","w")
	if pass1 == pass2:
		pl = list(pass1)
		ep = ""
		key = 20
		for x in pl:
			x = ord(x)^key
			ep = ep+chr(x)
		p.write(ep)
		print("password is saved!")
	else:
		print("error!")
	p.close()

def decode_pass(pass1):
	pl = list(pass1)
	dp = ""
	key = 20
	for x in pl:
		x = ord(x)^key
		dp = dp+chr(x)
	return dp


def locker(path,status):
	key =15
	f = open(path,"rb")
	file = f.read()
	f.close()

	file = bytearray(file)

	for index , value in enumerate(file):
		file[index] = value^key

	f = open(path,"wb")
	f.write(file)
	f.close()


	if status == "lo":

		log = open("log/log.txt","a")
		log.write(path+" ------------------- locked  \n\n ")
		log.close()
		print(path+" is locked!")

	elif status == "un":


		log = open("log/log.txt","a")
		log.write(path+" ------------------- unlocked  \n\n ")
		log.close()
		print(path+" is unlocked!")
		



def log():
	log = open("log/log.txt","r")
	alllog = log.read()
	log.close()
	print (alllog)


