import socket

def network_info():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    print("\n--- Network Information ---")
    print("Hostname :", hostname)
    print("IP Addr  :", ip)
