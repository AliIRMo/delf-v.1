import subprocess
import sys
import os
import color



def cmd():
    color.simple()
    print ("for Exit enter 5")
    print("""\n
=============================
**     developer : Ali     **
**                         **  
**  WELCOME TO CMD MODE !  **
**                         **
**    insta : alimoio0     **
=============================
""")
    while True:
        try:
            a = input("command : >>> ")
            s = subprocess.getoutput(a)
            print(s)
            if a == "5":
                os.system("cls")
                input("enter any key")
            
            break
        except:
            print("Error")
        
        
        
            


           
        
                
                
        
