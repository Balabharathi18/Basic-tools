import base64 as b
import subprocess
import os
import urllib.parse as u
import  binascii as bi




          # Function for Base64 encoder
def bas64_encoder():
    subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
    print("""
█▄▄ ▄▀█ █▀ █▀▀ █▄▄ █░█   █▀▀ █▄░█ █▀▀ █▀█ █▀▄ █▀▀ █▀█
█▄█ █▀█ ▄█ ██▄ █▄█ ▀▀█   ██▄ █░▀█ █▄▄ █▄█ █▄▀ ██▄ █▀▄""")
    val=input("Enter the input string to encode:")
    bin=val.encode('utf-8')
    base64_encoder=b.b64encode(bin)
    return base64_encoder

         # Function for URL Encoder
def url_encoder():
    subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
    print("""
█████████████████████████████████████████████████████████████████
█▄─██─▄█▄─▄▄▀█▄─▄█████▄─▄▄─█▄─▀█▄─▄█─▄▄▄─█─▄▄─█▄─▄▄▀█▄─▄▄─█▄─▄▄▀█
██─██─███─▄─▄██─██▀████─▄█▀██─█▄▀─██─███▀█─██─██─██─██─▄█▀██─▄─▄█
▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀""")
    val=input("Enter the input string to encode:")
    url_encode=u.quote(val)
    return url_encode
          
         # Function for Hex Encoder
def hex_encoder():
    subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
    print("""
░█─░█ ░█▀▀▀ ▀▄░▄▀ 　 ░█▀▀▀ ░█▄─░█ ░█▀▀█ ░█▀▀▀█ ░█▀▀▄ ░█▀▀▀ ░█▀▀█ 
░█▀▀█ ░█▀▀▀ ─░█── 　 ░█▀▀▀ ░█░█░█ ░█─── ░█──░█ ░█─░█ ░█▀▀▀ ░█▄▄▀ 
░█─░█ ░█▄▄▄ ▄▀░▀▄ 　 ░█▄▄▄ ░█──▀█ ░█▄▄█ ░█▄▄▄█ ░█▄▄▀ ░█▄▄▄ ░█─░█""")
    val=input("Enter the input string to encode:")
    bin=val.encode('utf-8')
    asci_encode=bi.hexlify(bin)
    return asci_encode
         
         # Function for Ascii Encoder
def asci_encoder():
    subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
    print("""
▄▀█ █▀ █▀▀ █ █   █▀▀ █▄░█ █▀▀ █▀█ █▀▄ █▀▀ █▀█
█▀█ ▄█ █▄▄ █ █   ██▄ █░▀█ █▄▄ █▄█ █▄▀ ██▄ █▀▄""")
    val=input("Enter the input to encode:")
    encoded = [ord(c) for c in val]
    for i in encoded:
        print(i,end=" ")
    return



# val="balabahrathi=ls/etc/usr/share"
# print(asci_encoder(val))

