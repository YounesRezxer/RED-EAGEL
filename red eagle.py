import time
from modules import banner
from modules import smsbomber
from colorama import Fore
import sys
import os

# شروع 

while True:
    try:
    
        banner.Banner1()
        banner.Infolest1()
        Option_name = input(Fore.RED+"   ┌─["+Fore.RED+"RED."+ Fore.LIGHTCYAN_EX + "EAGLE"  + Fore.RED + "]" + Fore.RED+"""
   └──╼ """+Fore.MAGENTA +">" +Fore.LIGHTBLUE_EX + ">" + Fore.GREEN + "> " +  Fore.RED + "").lower()
    except KeyboardInterrupt:
        print("")
        sys.exit()


    try:
        if Option_name == "1":
            time.sleep(0.1)
            banner.Banner1()
            banner.SMS_Bomb()
            input1 = input(Fore.RED+"   ┌─["+Fore.RED+"RED.EAGLE"+ Fore.LIGHTWHITE_EX + "/" + Fore.LIGHTCYAN_EX + "Anon SMS Bomb" + Fore.RED + "]" + Fore.RED+"""
   └──╼ """+Fore.MAGENTA +">" +Fore.LIGHTBLUE_EX + ">" + Fore.GREEN + "> " +  Fore.RED + "").lower()
            
            if input1 == "1":
                time.sleep(0.1)
                banner.Banner1()
                smsbomber.bomber()

            elif input1 == "2":
                time.sleep(0.2)
                os.system('python3 red.eagle.py')

            elif input1 == "3":
                time.sleep(0.02)
                sys.exit()

    except KeyboardInterrupt:
        print("")
        sys.exit()
    

    try:
        if Option_name == "2":
            time.sleep(0.1)
            banner.Banner1()
            banner.Developer()
            input(Fore.RED + "   [-]" + Fore.LIGHTCYAN_EX + " Press Enter To Menu ... ")

    except KeyboardInterrupt:
        print("")
        sys.exit()


    if Option_name == "3":
        time.sleep(0.2)
        print("")
        sys.exit()        

        