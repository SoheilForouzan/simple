import os

passwd = "soheil2003"

def main(key):
    if key == passwd:
        exit
    else:
        os.remove("help.txt")

if __name__ == "__main__":
    main(input("enter password >>>> "))
