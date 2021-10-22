Domains = [
    'www.facebook.com',  'facebook.com',  
    'www.youtube.com', 'youtube.com',
    'www.gmail.com', 'gmail.com',
    'www.digikala.com', 'digikala.com'
]

with open('/etc/hosts', 'r+') as hostfile:
    hosts = hostfile.readlines()
    hostfile.seek(0)
    for host in hosts:
        if not any(site in host for site in Domains):
            hostfile.write(host)
    hostfile.truncate()
print("[+] Connections Enabled!")
