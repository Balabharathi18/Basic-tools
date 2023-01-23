import subprocess,os
from decoders.decoder import URL_decoder, asci_decoder, bas64_decoder, hex_decoder


def decode():
    print("""
██████╗░░█████╗░░██████╗██╗░█████╗░  ██████╗░███████╗░█████╗░░█████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██║██╔══██╗  ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╦╝███████║╚█████╗░██║██║░░╚═╝  ██║░░██║█████╗░░██║░░╚═╝██║░░██║██║░░██║█████╗░░██████╔╝
██╔══██╗██╔══██║░╚═══██╗██║██║░░██╗  ██║░░██║██╔══╝░░██║░░██╗██║░░██║██║░░██║██╔══╝░░██╔══██╗
██████╦╝██║░░██║██████╔╝██║╚█████╔╝  ██████╔╝███████╗╚█████╔╝╚█████╔╝██████╔╝███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░  ╚═════╝░╚══════╝░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
                                                                            [+]By Balabharathi18""")
    print("""Some of the Basic Encoders
            1.Base64 decoder
            2.URL decoder 
            3.ASCII decoder
            4.HEX decoder
            5.Exit""")
    select=int(input("select the Decoder:"))
    if(select==1):
        print(bas64_decoder())
        input("Enter to continue...")
        subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
        decode()
    elif(select==2):
        print(URL_decoder())
        input("Enter to continue...")
        subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
        decode()
    elif(select==3):
        print(asci_decoder())
        input("\nEnter to continue...")
        subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
        decode()
    elif(select==4):
        print(hex_decoder())
        input("Enter to continue...")
        subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
        decode()
    else:
        return
decode()