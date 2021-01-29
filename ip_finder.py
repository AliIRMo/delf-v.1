import requests
import ipapi
import time 
def ipfi():
    print('welcome to ip location')
    time.sleep(2)
    print('please Enter Key :))')
    input('')
    time.sleep(2)
    inf = input('please ENTER ip address : > >  ')
    try:
        source = ipapi.location(ip=inf, key=None, )
        print('Ip :>>> ' + source["ip"])
        time.sleep(0.5)
        print("City :>>> " + source['city'])
        time.sleep(0.5)
        print('Region :>>> ' + source["region"])
        time.sleep(0.5)
        print('Country :>>> ' + source["country"])
        time.sleep(0.5)
        print('Country Name :>>>> '+ source["country_name"])
        time.sleep(0.5)
        print('Country calling code :>>> ' + source['country_calling_code'])
        time.sleep(0.5)
        print('Languages :>>> ' + source["languages"])
        time.sleep(0.5)
        print('Org :>>> ' + source["org"])
        input('for exit press any key :> > >')
    except:
        print("you have connection problem ! ")
