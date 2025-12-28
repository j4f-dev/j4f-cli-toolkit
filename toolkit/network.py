import socket
import os
import subprocess
from colorama import Fore, Style

def ip_info():
    host = input("Enter domain or IP: ")
    try:
        ip = socket.gethostbyname(host)
        print(f"\nIP Address: {ip}\n")
    except:
        print("Invalid domain/IP")

def ping_test():
    host = input("Enter IP or domain: ")
    os.system(f"ping -c 4 {host}")

def dns_lookup():
    domain = input("Enter domain: ")
    try:
        print(socket.gethostbyname_ex(domain))
    except:
        print("DNS lookup failed")

def common_port_scan():
    target = input("Enter IP: ")
    ports = [21,22,23,25,53,80,110,139,143,443,445,8080]
    print("\nScanning common ports...\n")

    for port in ports:
        s = socket.socket()
        s.settimeout(0.5)
        try:
            s.connect((target, port))
            print(f"[OPEN] Port {port}")
        except:
            pass
        s.close()

def advanced_port_scan():
    target = input("Enter IP: ")
    start = int(input("Start port: "))
    end = int(input("End port: "))

    print(f"\nScanning ports {start}-{end}...\n")

    for port in range(start, end + 1):
        s = socket.socket()
        s.settimeout(0.3)
        try:
            s.connect((target, port))
            print(f"[OPEN] Port {port}")
        except:
            pass
        s.close()

def network_menu():
    while True:
        print(Fore.GREEN + "\n[1] IP Information")
        print("[2] Ping Test")
        print("[3] DNS Lookup")
        print("[4] Port Scan (Common)")
        print("[5] Advanced Port Scan")
        print("[6] Back" + Style.RESET_ALL)

        choice = input("\nnet > ")

        if choice == "1":
            ip_info()
        elif choice == "2":
            ping_test()
        elif choice == "3":
            dns_lookup()
        elif choice == "4":
            common_port_scan()
        elif choice == "5":
            advanced_port_scan()
        elif choice == "6":
            break
        else:
            print("Invalid option")
