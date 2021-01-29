import socket
import time
import sys 
def bypass():



    print('hello dear')
    host = input('enter adress : >>> ')
    if host == '':
        print('please enter adress ;)  ')
        time.sleep(5)
        sys.exit()
    subdom = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']
    for sub in subdom:
        try:
            site = str(sub) + "." + host
            bypass = socket.gethostbyname(str(site))
            print (" [!] CloudFlare Bypass " + str(bypass) + ' | ' + str(site))
        except Exception:
            pass
    
    input('enter for exit :>> ')





