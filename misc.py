## misc.py - Useful module of claymore 
# -*- coding: utf-8 -*-
##
import os
import sys

__banner__ = """
\033[1;37m          ,       
\033[1;37m      _,-""-._    
\033[1;37m    ,'        '.  
\033[1;37m   / \033[1;31m   ,-,  ,-\033[1;37m \ \033[0m
\033[1;37m  |  \033[1;31m  /   \ | o| \033[0m
\033[1;37m  \  \033[1;31m  `-o-'  `-'                              
\033[1;37m   `,   _.--'`'--`\033[1;31m       
\033[1;37m     `--`---'  \033[1;31m        
\033[1;37m       ,' '    \033[1;31m   
\033[1;37m     ./ ,  `,  \033[1;31m   
\033[1;37m     / /     \  \033[1;37m       Made with \033[1;31m@\033[0m\033[1;37m by C L A Y Hacker Team\033[0m
\033[1;37m    (_)))_ _," \033[0m
\033[1;37m        ||||       Mr_Xd0wnz - Mr.n13- Mr.Kancil-DC\033[0m
\033[1;37m       _||||_,    Mr.Gh00st - R00T - Kintil39\033[0m
\033[1;37m------(_,-._)))-----------------------------------------\033[0m
"""
backtomenu_banner = """
  99) Return back to main menu
  00) Exit
"""
netcatrat_menubanner = """
  01) Generate Payload
  02) Start a Listener
"""

def netcatrat_menu():
	print netcatrat_menubanner

def logo():
	print __banner__

def clearscreen():
	if sys.platform == "linux2":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print backtomenu_banner
	backtomenu = raw_input("claymore > ")
	
	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print "\nERROR: Wrong input"
		time.sleep(2)
		restart_program()