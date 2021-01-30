
import os
import color
import time
import requests


    
        


def req():
    os.system("cls")
    color.simple()
    time.sleep(0.1)
    print('''\n
                WELCOME
    ===================================
    **                               **
    ** 1 - get                       **
    **                               **
    **                               **
    ** 2 - post                      **
    **                               **
    **                               **
    ** 3 - http-header               **
    **                               **
    ===================================
    ''')
    def get():
        try:
            k = input("[+] enter site address : >> ")
            if "http" or "https" in k:
                try:
                    re = requests.get(k)
                    if re == "200":
                        print("[+] page find ! ")
                    else:
                        print("[-] page not found ! ")
                except:
                    print("error ! ")        
            else:
                k = "http://" + k
                re = requests.get(k)
                if re == "200":
                    print('[+] page find ! ')
                else:
                    print("page not found ! ")
        except:
            print("you have connectio problem ! ")
            input('')


    def post():
        k2 = input("[+] Enter site adress : >> ")
        data = input ("enter data  : >>> ")
        try:
            if 'http' or 'https' in k2:
                re1 = requests.post(k2 , data)
                print(re1) 
            else:
                k2 = 'http://' + k2
                re1 = requests.post(k2 , data)
                print(re1)
        except:
            print(" you have connection problem ! ")
            input('')
    

    def http():
        while True:
            try:
                os.system("cls")
                color.simple()
                print('for back to menu press enter')
                k3 = input('[+] enter site address : >> ')
                if k3 == "":
                    break
                if 'http' or 'https' in k3:
                    res = requests.get("https://api.hackertarget.com/httpheaders/?q=" + k3).text
                    print(res)
                else:
                    k3 = "http://" + k3
                    res = requests.get("https://api.hackertarget.com/httpheaders/?q=" + k3).text
                    print(res)
                input("press enter ")
            except:
                print("you have connection problem ! ")
                input('')




        

    r = input("Enter number : >> ")

    print("for back to menu press enter")

    if r == "1":
        get()

    if r == "2":
        post()
    
    if r == "3":
        http()
    if r == "":
        print('')
    


