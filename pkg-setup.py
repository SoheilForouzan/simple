import argparse
import os

# Terminal colors

reset_color = "\033[0m"
green = "\033[32m"
red = "\033[31m"
yellow = "\033[93m"
cyan = "\033[36m"

# Python packages only for linux

python = [
    "django", "kivy", "flask",
    "pillow", "flask", "ipython",
    "selenium", "scapy", "whois",
    "pandas", "pytelegrambotapi",
    "telebot", "python-dotenv", "autopep8",
    "secure-smtplib", "pyperclip3", "random2",
    "paramiko", "opencv-python", "scipy",
    "bs4", "datetime",
]

# Termux section
termux_start = [
    "termux-setup-storage", "apt update", "apt upgrade",
]

termux_install = [
    "coreutils", "openssh", "git",
    "tor", "neofetch", "unstable-repo",
    "x11-repo", "python-pip", "zsh"
]

termux_py = [
    "ipython", "scapy", "whois",
    "pytelegrambotapi", "telebot", "python-dotenv",
    "secure-smtplib", "pyperclip3", "random2",
    "datetime", "bs4", "paramiko"
]

# Script Flags

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--linux",
                    help="linux pkgs")

parser.add_argument("-t", "--termux",
                    help="termux pkgs")
args = parser.parse_args()


# Linux Python pkg installation

def python_pkgs():
    for pkg in python:
        print(cyan + pkg + reset_color)
    print("\n")
    starting = ""
    while (starting != "y" and starting != "n"):
        starting = input("[?] Start instalation? (y -> yes, n -> no) ")
    if starting == "y" or starting == "Y":
        print(f"{green}[+] started{reset_color}\n")
        for pkg in python:
            print(f"{yellow}[*]{pkg}:{reset_color}")
            os.system(f"pip install {pkg}")
            print(f"{green}[+] Task Done!{reset_color}\n")

    elif starting == "n" or starting == "N":
        print(f"{red}[X] Canceled!{reset_color}")

# Termux Settings Setup

def termux_setup():
    for command in termux_start:
        print(cyan + command + reset_color)
    print("\n")
    starting = ""
    while (starting != "y" and starting != "n"):
        starting = input("[?] Start Setup? (y -> yes, n -> no) ")
    if starting == "y" or starting == "Y":
        print(f"{green}[+] started{reset_color}\n")
        for command in termux_start:
            print(f"{yellow}[*]{command}:{reset_color}")
            os.system(command)
            print(f"{green}[+] Task Done!{reset_color}\n")

    elif starting == "n" or starting == "N":
        print(f"{red}[X] Canceled!{reset_color}")

# Termux requirements installation

def termux_requirements():
    for requirement in termux_install:
        print(cyan + requirement + reset_color)
    print("\n")
    starting = ""
    while (starting != "y" and starting != "n"):
        starting = input("[?] Start instalation? (y -> yes, n -> no) ")
    if starting == "y" or starting == "Y":
        print(f"{green}[+] started{reset_color}\n")
        for requirement in termux_install:
            print(f"{yellow}[*]{requirement}:{reset_color}")
            os.system(f"apt install {requirement}")
            print(f"{green}[+] Task Done!{reset_color}\n")

    elif starting == "n" or starting == "N":
        print(f"{red}[X] Canceled!{reset_color}")

# Termux python dependencies

def termux_python():
    for pkg in termux_py:
        print(cyan + pkg + reset_color)
    print("\n")
    starting = ""
    while (starting != "y" and starting != "n"):
        starting = input("[?] Start instalation? (y -> yes, n -> no) ")
    if starting == "y" or starting == "Y":
        print(f"{green}[+] started{reset_color}\n")
        for pkg in termux_install:
            print(f"{yellow}[*]{pkg}:{reset_color}")
            os.system(f"pip install {pkg}")
            print(f"{green}[+] Task Done!{reset_color}\n")

    elif starting == "n" or starting == "N":
        print(f"{red}[X] Canceled!{reset_color}")


def main():
	# Linux

    if args.linux == "py":
        python_pkgs()

	# Termux

    if args.termux == "setup":
        termux_setup()
    elif args.termux == "requirements":
        termux_requirements()
    elif args.termux == "py":
        termux_python()


if __name__ == "__main__":
    main()
