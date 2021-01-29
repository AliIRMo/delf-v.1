import color
import time
import os
import subprocess
import cmdm
import sys
import helpinf
import cloud
import ip_finder
import net
import who
import dnslo
import sec



import datetime
while True:
    os.system("cls")
    #custom
    color.simple()
    
    x = datetime.datetime.now()
    print("time and date is : ")
    print(x)

    time.sleep(0.1)

    
    print('''\n
==============================================
**  Welcome to Delf What can i do for you?? **
**  -------------------###                  **
**  1-cmd_mode                              **
**  -------------------###                  **
**  2- developer                            **
**  -------------------###                  **
**  3-customize                             **
**  -------------------###                  **
**  4-tools                                 **
**  -------------------###                  **
==============================================                                       
''')              
        
    a = input("Enter number :>>> ")


    

#________________________________________#

    if a == "1":
        
        os.system("cls")
        cmdm.cmd()
        #____________#

    if a == "2":
        helpinf.infor2()
        i2 = input("Press Enter >>  ")
        
        
        #____________#
        
    if a == "3":
        helpinf.infor3()
        #____________#

    if a == "4":
        helpinf.infor4()
        t2 = input("enter number :>>> ")
        if t2 == "1":
            cloud.bypass()
        if t2 == "2":
            ip_finder.ipfi()
        if t2 == "3":
            net.req()
        if t2 == "4":
            who.whois()
        if t2 == "5":
            dnslo.dnsl()
        if t2 == "6":
            sec.xss()



        #____________#
    if a == "":
        print("GOOD Luck!  :)")
        sys.exit()

        

        
        
        

#________________________________________#


        
        
        
    
