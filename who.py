import requests
import os
import color
import socket
def whois():
    os.system("cls")

    color.simple()
    print('''\n
    ================================
                WELCOME
    ================================
    enter site address : >> |
                            |
                            V''')
    i = input("enter site address :>> ")
    try:


        if "http" or "https" in i:
            d = socket.gethostbyname(i)
        else:
            i = "http://" + i
            d = socket.gethostbyname(i)
    
        re = requests.get("https://api.hackertarget.com/whois/?q=" + d).text
        print (re)

    except:
        print("you have connection problem ! ")
    