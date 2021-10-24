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

# Termux section
termux_setup = [
	'termux-setup-storage','apt update', 'apt upgrade',
]

termux_install = [
	'coreutils', 'openssh', 'git',
	'tor', 'neofetch','unstable-repo',
	'x11-repo', 'python', 'python-pip'
]
termux_python = [
	'ipython', 'scapy', 'whois',
	'pytelegrambotapi', 'telebot', 'python-dotenv',
	'secure-smtplib', 'pyperclip3', 'random2',
	'datetime', 'bs4', 'paramiko'
]

# Flags
parser = argparse.ArgumentParser()

parser.add_argument("-l", "--linux",
                    help="linux pkgs")

parser.add_argument("-t", "--termux",
                    help="termux pkgs")
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

# Termux Settings Setup

def termux_setup():
	for task in termux_setup:
		print(task)
	print("\n")
	starting = ''
	while (starting != 'y' and starting != 'n'):
		starting = input('[?] Start Setup? (y -> yes, n -> no) ')
	if starting == "y" or starting == "Y":
		print(f"{green}[+] started{reset_color}\n")
		for task in termux_setup:
			print(f'{yellow}[*]{task}:{reset_color}')
			os.system(task)
			print(f'{green}[+] Task Done!{reset_color}\n')
			
	elif starting == "n" or starting == "N":
		print(f"{red}[X] Canceled!{reset_color}")

# Termux requirements installation

def termux_requirements():
	for task in termux_install:
		print(task)
	print("\n")
	starting = ''
	while (starting != 'y' and starting != 'n'):
		starting = input('[?] Start instalation? (y -> yes, n -> no) ')
	if starting == "y" or starting == "Y":
		print(f"{green}[+] started{reset_color}\n")
		for task in termux_install:
			print(f'{yellow}[*]{task}:{reset_color}')
			os.system(f'apt install {task}')
			print(f'{green}[+] Task Done!{reset_color}\n')
			
	elif starting == "n" or starting == "N":
		print(f"{red}[X] Canceled!{reset_color}")

# Termux python dependencies

def termux_python():
	for task in termux_python:
		print(task)
	print("\n")
	starting = ''
	while (starting != 'y' and starting != 'n'):
		starting = input('[?] Start instalation? (y -> yes, n -> no) ')
	if starting == "y" or starting == "Y":
		print(f"{green}[+] started{reset_color}\n")
		for task in termux_install:
			print(f'{yellow}[*]{task}:{reset_color}')
			os.system(f'pip install {task}')
			print(f'{green}[+] Task Done!{reset_color}\n')
			
	elif starting == "n" or starting == "N":
		print(f"{red}[X] Canceled!{reset_color}")


def main():
	if args.linux == "py":
		python_pkgs()
	if args.termux == "setup":
		termux_setup()
	elif args.termux == "requirements":
		termux_requirements()
	elif args.termux == "python":
		termux_python()


if __name__ == '__main__':
	main()
	