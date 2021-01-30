import os
import color
import requests

def xss():

        try:
            os.system('cls')
            color.simple()
            print("Welcome")
            ad = input("enter site adrress :>> ")

            if 'http' or 'https' in ad:
                req3 = requests.get(ad)
                if req3 == '200':
                    print('[+] This site has security problem (xss) !')
                else:
                    print('[-] this site is safe !')

            else:
                ad = 'http' + ad
                req3 = requests.get(ad)

                if req3 == "200":
                    print("[+] This site has security problem ! ")

                if req3 != '200':
                    print("[-] This site is safe")
        except:
            print("You have connection problem !")
            input('')