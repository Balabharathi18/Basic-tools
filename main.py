# from unittest import main
import subprocess,os
from encoders.enocders import hex_encoder, bas64_encoder, url_encoder,asci_encoder

def encode():
    print("""
██████╗░░█████╗░░██████╗██╗░█████╗░  ███████╗███╗░░██╗░█████╗░░█████╗░██████╗░███████╗██████╗░░██████╗
██╔══██╗██╔══██╗██╔════╝██║██╔══██╗  ██╔════╝████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝
██████╦╝███████║╚█████╗░██║██║░░╚═╝  █████╗░░██╔██╗██║██║░░╚═╝██║░░██║██║░░██║█████╗░░██████╔╝╚█████╗░
██╔══██╗██╔══██║░╚═══██╗██║██║░░██╗  ██╔══╝░░██║╚████║██║░░██╗██║░░██║██║░░██║██╔══╝░░██╔══██╗░╚═══██╗
██████╦╝██║░░██║██████╔╝██║╚█████╔╝  ███████╗██║░╚███║╚█████╔╝╚█████╔╝██████╔╝███████╗██║░░██║██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░  ╚══════╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░
                                                                                    [+]By Balabharathi18""")
    print("""Some of the Basic Encoders
            1.Base64 encoder
            2.URL encoder 
            3.ASCII encoder
            4.HEX encoder
            5.Exit""")
    select=int(input("select the Encoder:"))
    if(select==1):
        print(bas64_encoder())
        input("Enter to continue...")
        subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
        encode()
    elif(select==2):
        print(url_encoder())
        input("Enter to continue...")
        subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
        encode()
    elif(select==3):
        asci_encoder()
        input("\nEnter to continue...")
        subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
        encode()
    elif(select==4):
        print(hex_encoder())
        input("Enter to continue...")
        subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
        encode()
    else:
        return
encode()




