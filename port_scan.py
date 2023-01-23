import socket
pt=[]
def port_scan(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0)
        result = sock.connect_ex((ip, port))
        if result == 0:
            pt.append(port)
            print("Port {} is open".format(port))
        else:
            print("Port {} is closed".format(port))
            pass
        sock.close()
    except:
        print("Error occurred during port scan")
        

def ip_scan(ip):
    for port in range(1,80):
        port_scan(ip, port)
    print(pt)

ip_to_scan = input("Enter the IP address to scan: ")
ip_scan(ip_to_scan)