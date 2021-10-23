import argparse
import os

reset_color = '\033[0m'
green = '\033[32m'
red = '\033[31m'
yellow='\033[93m'

python = [
    'django', 'kivy', 'flask',
	'pillow', 'flask', 'ipython',
	'selenium', 'scapy', 'whois',
	'pandas', 'pytelegrambotapi',
	'telebot', 'python-dotenv', 'autopep8',
	'secure-smtplib', 'pyperclip3','random2',
	'paramiko', 'opencv-python','scipy',
	'bs4', 'datetime',
]

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--install",
                    help="install pkg List")

args = parser.parse_args()


if args.install == "py":
	for pkg in python:
		print(pkg)
	print('\n')
	starting = input('[?] Start instalation? (y -> yes, n -> no) ')
	if starting == "y" or "Y":
		print(f"{green}[+] started{reset_color}\n")
		for pkg in python:
			print(f'{yellow}[*]{pkg}:{reset_color}')
			os.system(f"pip install {pkg}")
			print(f'{green}[+] Task Done!{reset_color}\n')
	elif starting == "n" or "N":
		print(f"{red}[X] Canceled!{reset_color}")
		exit()
	else:
		print(f"{red}[X] Not defined!{reset_color}")