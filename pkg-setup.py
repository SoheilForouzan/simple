import argparse
import os

# terminal colors

reset_color = '\033[0m'
green = '\033[32m'
red = '\033[31m'
yellow='\033[93m'

# Python packages only for linux

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

# Flags
parser = argparse.ArgumentParser()

parser.add_argument("-i", "--install",
                    help="install pkg List")

args = parser.parse_args()


# Python pkg installation

def python_pkgs():
	for pkg in python:
		print(pkg)
	print('\n')
	starting = ''
	while (starting != 'y' and starting != 'n'):
		starting = input('[?] Start instalation? (y -> yes, n -> no) ')
	if starting == "y" or starting == "Y":
		print(f"{green}[+] started{reset_color}\n")
		for pkg in python:
			print(f'{yellow}[*]{pkg}:{reset_color}')
			os.system(f"pip install {pkg}")
			print(f'{green}[+] Task Done!{reset_color}\n')
			
	elif starting == "n" or starting == "N":
		print(f"{red}[X] Canceled!{reset_color}")
		exit()
	else:
		print(f"{red}[X] Not defined!{reset_color}")

def main():
	if args.install == "py":
		python_pkgs()

if __name__ == '__main__':
	main()