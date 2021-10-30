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
    "pkg update", "pkg upgrade", "termux-setup-storage"
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
    "datetime", "bs4", "paramiko",
    "requests"
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
        for pkg in track(python, description="Installing..."):
            print(f"{yellow}[*]{pkg}:{reset_color}")
            os.system(f'pip install {pkg}')
            print(f"{green}[+] Task Done!{reset_color}\n")

    elif starting == "n" or starting == "N":
        print(f"{red}[X] Canceled!{reset_color}")
    else:
        python_pkgs()

# Package installation for arch linux


def arch_setup():
    starting = input("[?] Start instalation? [Y/n] ") or "Y"

    if starting == "y" or starting == "Y":
        print(f"{green}[+] started{reset_color}\n")
        for pkg in track(arch_pkgs, description="Installing..."):
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
        for command in track(termux_start, description="Installing..."):
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
        for requirement in track(termux_install, description="Installing..."):
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
        for pkg in track(termux_py, description="Installing..."):
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
        try:
            for pkg in python:
                print(cyan + pkg + reset_color)
            print("\n")
            python_pkgs()
        except KeyboardInterrupt:
            print(f"\n{red}[X] Canceled!{reset_color}")
    # Arch Linux

    if args.arch == "pkgs":
        try:
            if os.geteuid() == 0:
                for pkg in arch_pkgs:
                    print(cyan + pkg + reset_color)
                print("\n")
                arch_setup()
            else:
                print(
                    f"{yellow}[!] Run as root in order to work currectly!{reset_color}\n")
        except KeyboardInterrupt:
            print(f"\n{red}[X] Canceled!{reset_color}")
    # Termux

    if args.termux == "setup":
        try:
            for command in termux_start:
                print(cyan + command + reset_color)
            print("\n")
            termux_setup()
        except KeyboardInterrupt:
            print(f"\n{red}[X] Canceled!{reset_color}")

    elif args.termux == "requirements":
        try:
            for requirement in termux_install:
                print(cyan + requirement + reset_color)
            print("\n")
            termux_requirements()
        except KeyboardInterrupt:
            print(f"\n{red}[X] Canceled!{reset_color}")

    elif args.termux == "py":
        try:
            for pkg in termux_py:
                print(cyan + pkg + reset_color)
            print("\n")
            termux_python()
        except KeyboardInterrupt:
            print(f"\n{red}[X] Canceled!{reset_color}")

    elif args.termux == "arch":
        try:
            print(f'{cyan} Installation of arch linux for termux {reset_color}')
            print("\n")
            arch_termux()
        except KeyboardInterrupt:
            print(f"\n{red}[X] Canceled!{reset_color}")

    else:
        print(f'{red}[X] Nothing to do!{reset_color}')


if __name__ == "__main__":
    os.system("pip install rich")
    from rich.progress import track

    main()
