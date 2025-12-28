import os
import socket
import platform
import subprocess
from toolkit.colors import Color


# ---------------- IP INFORMATION ----------------
def ip_info():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        print(Color.CYAN + f"\nHostname : {hostname}")
        print(f"Local IP : {local_ip}\n" + Color.RESET)

    except Exception as e:
        print(Color.RED + f"Error: {e}" + Color.RESET)


# ---------------- PING TEST ----------------
def ping_test():
    host = input(Color.YELLOW + "Enter host to ping: " + Color.RESET)

    if platform.system().lower() == "windows":
        cmd = ["ping", "-n", "4", host]
    else:
        cmd = ["ping", "-c", "4", host]

    try:
        subprocess.run(cmd)
    except Exception as e:
        print(Color.RED + f"Ping failed: {e}" + Color.RESET)


# ---------------- DNS LOOKUP ----------------
def dns_lookup():
    domain = input(Color.YELLOW + "Enter domain: " + Color.RESET)

    try:
        ip = socket.gethostbyname(domain)
        print(Color.CYAN + f"\nDomain : {domain}")
        print(f"IP     : {ip}\n" + Color.RESET)
    except Exception:
        print(Color.RED + "DNS lookup failed!" + Color.RESET)


# ---------------- PORT SCAN (COMMON) ----------------
def port_scan():
    target = input(Color.YELLOW + "Enter target IP/domain: " + Color.RESET)
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445]

    print(Color.CYAN + "\nScanning common ports...\n" + Color.RESET)

    for port in common_ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(Color.GREEN + f"[OPEN] Port {port}" + Color.RESET)
            s.close()
        except:
            pass


# ---------------- ADVANCED PORT SCAN ----------------
def advanced_port_scan():
    target = input(Color.YELLOW + "Enter target IP/domain: " + Color.RESET)
    start = int(input("Start port: "))
    end = int(input("End port: "))

    print(Color.CYAN + f"\nScanning ports {start}-{end}...\n" + Color.RESET)

    for port in range(start, end + 1):
        try:
            s = socket.socket()
            s.settimeout(0.3)
            result = s.connect_ex((target, port))
            if result == 0:
                print(Color.GREEN + f"[OPEN] Port {port}" + Color.RESET)
            s.close()
        except:
            pass


# ---------------- NETWORK MENU ----------------
def network_info():
    while True:
        print(Color.GREEN + "\n[1] IP Information")
        print("[2] Ping Test")
        print("[3] DNS Lookup")
        print("[4] Port Scan (Common)")
        print("[5] Advanced Port Scan")
        print("[6] Back" + Color.RESET)

        choice = input(Color.YELLOW + "\nnet > " + Color.RESET)

        if choice == "1":
            ip_info()

        elif choice == "2":
            ping_test()

        elif choice == "3":
            dns_lookup()

        elif choice == "4":
            port_scan()

        elif choice == "5":
            advanced_port_scan()

        elif choice == "6":
            return

        else:
            print(Color.RED + "Invalid option!" + Color.RESET)
