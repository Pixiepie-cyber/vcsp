import time
import scapy
import os
from colorama import init, Fore, Back, Style
from settings import *
init()

def main():
		
	os.system("@echo off")
	os.system("cls")

	auth = None
	passwd = input("Enter THE password: ")

	if passwd.lower() == "anonymous":
		print(green + "Correct password, enjoy!!" + white)
		os.system("pause")
		auth = True
	else:
		print(red + "Wrong password, try again later!!" + white)
		exit()

	while auth:
		os.system("cls")

		print('Welcome to:')

		print("\033[31m____   _____________             ___________________ ")
		print("\033[33m\\   \\ /   /\\_   ___ \\           /   _____/\\______   \\")
		print("\033[93m \\   Y   / /    \\  \\/   ______  \\_____  \\  |     ___/")
		print("\033[32m  \\     /  \\     \\____ /_____/  /        \\ |    |    ")
		print("\033[34m   \\___/    \\______  /         /_______  / |____|   \033[0m")

		print("\n" + green + "A" + cyan + " Virtual Cyber Security Program" + green + " designed to secure you online!!")

		print("\n" + 
			green + "All Rights Reserved To " + 
			magenta + " Clinton Gethi" + 
			green + " founder of" +
			magenta + " Gum Bee Tech" +
			green + ". \n \n")

		cmd = input(white + "["+ green + "Dev" + white + "]@[" + red + "VC-SP" + white + "]# ")

		if cmd.lower() == "exit":
			exit()

if __name__ == "__main__":
	main()
