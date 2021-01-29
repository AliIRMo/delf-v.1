import os
import requests
import color

def dnsl():
    os.system("cls")

    color.simple()
    print('''\n
===========================
            WELCOME     
===========================
enter domain :>>>|
                 |
                 V''')
    do = input("enter :>>> ")
    try:

        re = requests.get("https://api.hackertarget.com/dnslookup/?q=" + do).text

        print(re)
    except:
        print("you have connection problem ! ")