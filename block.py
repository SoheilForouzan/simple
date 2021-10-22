
Domains = [
    'www.facebook.com',  'facebook.com',  
    'www.youtube.com', 'youtube.com',
    'www.gmail.com', 'gmail.com',
    'www.digikala.com', 'digikala.com'
]
redirect = "127.0.0.1"

with open('/etc/hosts', 'r+') as hostfile:
                hosts = hostfile.read()
                for site in  Domains:
                    if site not in hosts:
                       hostfile.write(redirect+' '+site+'\n') 
print("[+] Connections Blocked!")   