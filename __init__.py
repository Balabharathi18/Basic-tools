import subprocess,os    


def hack_tools():
    subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
    print("""
█▀ █ █▀▄▀█ █▀█ █░░ █▀▀   █░█ ▄▀█ █▀▀ █▄▀   ▀█▀ █▀█ █▀█ █░░ █▀
▄█ █ █░▀░█ █▀▀ █▄▄ ██▄   █▀█ █▀█ █▄▄ █░█   ░█░ █▄█ █▄█ █▄▄ ▄█
                                                [+]By Balabharathi18""")
    print("""Some of the basic Tools
        1.Encoding Techinques
        2.Decoding Techinques
        3.Port Scanning
        4.Exit""")
    temp=int(input("Select required techinque:"))
    if(temp==1):
        subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
        from main import encode
        print("Enter to continue....")
        hack_tools()
    elif(temp==2):
        subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
        from main2 import decode
        print("Enter to Continue....")
        hack_tools()
    elif(temp==3):
        subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
        from port_scan import ip_scan
        print("Enter to coninue...")
        hack_tools()
    else:
        return
hack_tools()
