# code by sandakelum priyamantha
import main
import getpass
import sys

baner =  '''
 _               _             
| |    ___   ___| | _____ _ __ 
| |   / _ \ / __| |/ / _ \ '__|
| |__| (_) | (__|   <  __/ |   
|_____\___/ \___|_|\_\___|_|   v1.0

by
  sandakelum priyamantha


  (1) lock file
  (2) unlock file
  (3) change password
  (4) show locker log
  (0) exit

'''
print(baner)

ps = open("log/pass.spw","r")
l1 = ps.readline()
ps.close()

# print(main.decode_pass(l1))

if l1 == "":
	pass1 = getpass.getpass("enter new password : ")
	pass2 = getpass.getpass("enter password again : ")
	main.setpass(pass1,pass2)
	# main.locker("log/pass.txt","lo")

	while pass1 != pass2:
			pass1 = getpass.getpass("enter new password : ")
			pass2 = getpass.getpass("enter password again : ")
			main.setpass(pass1,pass2)
			# main.locker("log/pass.txt","lo")

			






choose = input("\nlocker > ")
while 1==1:

	if choose == "0":
		print("good bye!")
		sys.exit()
	elif choose == "1":
		print("[#]lock file\n")
		passl1 = getpass.getpass("enter your password : ")
		passl2 = main.decode_pass(l1)
		
		if passl1 == passl2 :
			filepath = input("input file path to lock : ")
			main.locker(filepath,"lo")
		else:
			print("invalid password! try again ")

	elif choose == "2":
		print("[#]unlock file\n")
		passl1 = getpass.getpass("enter your password : ")
		passl2 = main.decode_pass(l1)
		
		if passl1 == passl2 :
			filepath = input("input file path to unlock : ")
			main.locker(filepath,"un")
		else:
			print("invalid password! try again ")

	elif choose == "3":
		print("[#]change password\n")
		passl1 = getpass.getpass("enter your password : ")
		passl2 = main.decode_pass(l1)

		if passl1 == passl2 :
			passn1 = getpass.getpass("enter your new password : ")
			passn2 = getpass.getpass("enter your new password again : ")
			main.setpass(passn1,passn2)

		else:
			print("invalid password! try again ")

	elif choose == "4":
		print("[#] locker log \n")
		log = open("log/log.txt")
		print(log.read())
		log.close()






	# print(baner)
	choose = input("\nlocker > ")





  