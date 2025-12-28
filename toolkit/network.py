import socket
import os
from toolkit.utils import Color, slow_print

def ip_info():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    slow_print(Color.CYAN + f"\nHostname   : {hostname}")
    slow_print(f"Local IP   : {local_ip}\n" + Color.RESET)

def ping_test():
    target = input(Color.YELLOW + "Enter host (example: google.com): " + Color.RESET)
    print(Color.GREEN)
    os.system(f"ping -c 4 {target}")
    print(Color.RESET)

def dns_lookup():
    domain = input(Color.YELLOW + "Enter domain: " + Color.RESET)
    try:
        ip = socket.gethostbyname(domain)
        slow_print(Color.CYAN + f"\nDomain: {domain}")
        slow_print(f"IP     : {ip}\n" + Color.RESET)
    except socket.gaierror:
        slow_print(Color.RED + "DNS lookup failed!\n" + Color.RESET)

def port_scan():
    target = input(Color.YELLOW + "Target IP (example: 127.0.0.1): " + Color.RESET)
    slow_print(Color.CYAN + "\nScanning common ports...\n" + Color.RESET)

    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 8080]

    for port in common_ports:
        s = socket.socket()
        s.settimeout(0.5)
        try:
            s.connect((target, port))
            slow_print(Color.GREEN + f"[OPEN] Port {port}")
        except:
            pass
        s.close()

    print(Color.RESET)

def network_info():
    while True:
        print(Color.GREEN + """
[1] IP Information
[2] Ping Test
[3] DNS Lookup
[4] Port Scan
[5] Back
""" + Color.RESET)

        choice = input(Color.YELLOW + "net > " + Color.RESET)

        if choice == "1":
            ip_info()
        elif choice == "2":
            ping_test()
        elif choice == "3":
            dns_lookup()
        elif choice == "4":
            port_scan()
        elif choice == "5":
            break
        else:
            slow_print(Color.RED + "Invalid option!" + Color.RESET)
