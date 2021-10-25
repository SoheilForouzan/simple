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

arch_pkgs = [
    'neofetch', 'bpytop', 'htop',
    'tor', 'tmux', 'virtualbox',
    'preload', 'libreoffice-fresh', 'nmap',
    'geary', 'discord', 'discover',
    'android-tools', 'whois'
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

# Arch on termux

termux_arch = 'pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Arch/armhf/arch.sh && bash arch.sh'


# Script Flags

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--linux",
                    help="Linux pkgs")

parser.add_argument("-a", "--arch",
                    help="Arch pkgs")

parser.add_argument("-t", "--termux",
                    help="Termux pkgs")
args = parser.parse_args()


# Linux Python pkg installation

def python_pkgs():
    starting = input("[?] Start instalation? [Y/n] ") or "Y"

    if starting == "y" or starting == "Y":
        print(f"{green}[+] started{reset_color}\n")
        for pkg in python:
            print(f"{yellow}[*]{pkg}:{reset_color}")
            os.system(f'pip install {pkg}')
            print(f"{green}[+] Task Done!{reset_color}\n")

    elif starting == "n" or starting == "N":
        print(f"{red}[X] Canceled!{reset_color}")
    else:
        python_pkgs()


def arch_setup():
    starting = input("[?] Start instalation? [Y/n] ") or "Y"

    if starting == "y" or starting == "Y":
        print(f"{green}[+] started{reset_color}\n")
        for pkg in arch_pkgs:
            print(f"{yellow}[*]{pkg}:{reset_color}")
            os.system(f'pacman -S {pkg}')
            print(f"{green}[+] Task Done!{reset_color}\n")

    elif starting == "n" or starting == "N":
        print(f"{red}[X] Canceled!{reset_color}")
    else:
        python_pkgs()

    os.system("exit")
# Termux Settings Setup


def termux_setup():

    starting = input("[?] Start Setup? [Y/n] ") or "Y"
    if starting == "y" or starting == "Y":
        print(f"{green}[+] started{reset_color}\n")
        for command in termux_start:
            print(f"{yellow}[*]{command}:{reset_color}")
            os.system(command)
            print(f"{green}[+] Task Done!{reset_color}\n")

    elif starting == "n" or starting == "N":
        print(f"{red}[X] Canceled!{reset_color}")
    else:
        python_pkgs()

# Arch linux installation in termux


def arch_termux():

    starting = input("[?] Start Installation? [Y/n] ") or "Y"
    if starting == "y" or starting == "Y":
        print(f"{green}[+] started{reset_color}\n")
        print(f"{yellow}[*]{termux_arch}:{reset_color}")
        os.system(termux_arch)
        print(f"{green}[+] Task Done!{reset_color}\n")

    elif starting == "n" or starting == "N":
        print(f"{red}[X] Canceled!{reset_color}")
    else:
        python_pkgs()

# Termux requirements installation


def termux_requirements():
    starting = input("[?] Start instalation? [Y/n] ") or "Y"
    if starting == "y" or starting == "Y":
        print(f"{green}[+] started{reset_color}\n")
        for requirement in termux_install:
            print(f"{yellow}[*]{requirement}:{reset_color}")
            os.system(f"pkg install {requirement}")
            print(f"{green}[+] Task Done!{reset_color}\n")

    elif starting == "n" or starting == "N":
        print(f"{red}[X] Canceled!{reset_color}")
    else:
        python_pkgs()

# Termux python dependencies


def termux_python():

    starting = input("[?] Start instalation? [Y/n] ") or "Y"
    if starting == "y" or starting == "Y":
        print(f"{green}[+] started{reset_color}\n")
        for pkg in termux_py:
            print(f"{yellow}[*]{pkg}:{reset_color}")
            os.system(f"pip install {pkg}")
            print(f"{green}[+] Task Done!{reset_color}\n")

    elif starting == "n" or starting == "N":
        print(f"{red}[X] Canceled!{reset_color}")
    else:
        python_pkgs()


def main():
    # Linux

    if args.linux == "py":
        for pkg in python:
            print(cyan + pkg + reset_color)
        print("\n")
        python_pkgs()

    # Arch Linux

    if args.arch == "pkgs":
        if os.geteuid() == 0:
            for pkg in arch_pkgs:
                print(cyan + pkg + reset_color)
            print("\n")
            arch_setup()
        else:
            print(
                f"{yellow}[!] Run as root in order to work currectly!{reset_color}\n")

    # Termux

    if args.termux == "setup":
        for command in termux_setup:
            print(cyan + command + reset_color)
        print("\n")
        termux_setup()

    elif args.termux == "requirements":
        for requirement in termux_requirements:
            print(cyan + requirement + reset_color)
        print("\n")
        termux_requirements()

    elif args.termux == "py":
        for pkg in termux_py:
            print(cyan + pkg + reset_color)
        print("\n")
        termux_python()

    elif args.termux == "arch":
        print(f'{cyan} Installation of arch linux for termux {reset_color}')
        print("\n")
        arch_termux()

    else:
        print(f'{red}[X] Nothing to do!{reset_color}')


if __name__ == "__main__":
    main()
