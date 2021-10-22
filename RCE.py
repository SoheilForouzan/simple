import paramiko

hostname = "192.168.1.101"
username = "user"
password = "soheil20030617"

# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, port=8022, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

while (True):
    command = input("command > ")
    if command == "exit":
        exit()
    else:
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(err)