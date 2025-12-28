import socket

def network_info():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    print("\n🌐 NETWORK INFORMATION")
    print("-" * 25)
    print(f"Hostname : {hostname}")
    print(f"IP Addr  : {ip}")
