import socket
import subprocess
from toolkit.utils import Color, slow_print


# ================= IP INFORMATION =================
def ip_info():
    print(Color.CYAN + "\n--- IP INFORMATION ---")
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
    except:
        hostname = "Unknown"
        local_ip = "Unknown"

    print(f"Hostname : {hostname}")
    print(f"Local IP : {local_ip}\n" + Color.RESET)


# ================= PING TEST =================
def ping_test():
    target = input(Color.YELLOW + "Enter IP / Domain: " + Color.RESET)

    print(Color.CYAN + "\nPinging target...\n" + Color.RESET)
    try:
        subprocess.run(
            ["ping", "-c", "4", target],
            stdout=None,
            stderr=None
        )
    except:
        print(Color.RED + "Ping failed!" + Color.RESET)


# ================= DNS LOOKUP =================
def dns_lookup():
    domain = input(Color.YELLOW + "Enter domain: " + Color.RESET)
    try:
        ip = socket.gethostbyname(domain)
        print(Color.GREEN + f"\nDomain : {domain}")
        print(f"IP     : {ip}\n" + Color.RESET)
    except:
        print(Color.RED + "DNS lookup failed!\n" + Color.RESET)


# ================= COMMON PORT SCAN =================
def common_port_scan():
    target = input(Color.YELLOW + "Target IP / Domain: " + Color.RESET)
    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "TELNET",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        139: "NETBIOS",
        443: "HTTPS",
        445: "SMB",
        8080: "HTTP-ALT"
    }

    print(Color.CYAN + f"\nScanning common ports on {target}...\n" + Color.RESET)

    for port, service in common_ports.items():
        sock = socket.socket()
        sock.settimeout(0.5)
        try:
            sock.connect((target, port))
            print(Color.GREEN + f"[OPEN] {port} ({service})")
        except:
            pass
        finally:
            sock.close()

    print(Color.RESET)


# ================= ADVANCED PORT SCAN =================
def advanced_port_scan():
    target = input(Color.YELLOW + "Target IP / Domain: " + Color.RESET)

    try:
        start_port = int(input("Start Port: "))
        end_port = int(input("End Port: "))
    except ValueError:
        print(Color.RED + "Invalid port range!\n" + Color.RESET)
        return

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print(Color.RED + "Port range must be 1–65535\n" + Color.RESET)
        return

    print(Color.CYAN + f"\nScanning ports {start_port}-{end_port} on {target}\n" + Color.RESET)

    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket()
        sock.settimeout(0.3)
        try:
            sock.connect((target, port))
            open_ports.append(port)
            print(Color.GREEN + f"[OPEN] Port {port}")
        except:
            pass
        finally:
            sock.close()

    if not open_ports:
        print(Color.RED + "\nNo open ports found." + Color.RESET)

    print(Color.RESET)


# ================= NETWORK MENU =================
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
            common_port_scan()

        elif choice == "5":
            advanced_port_scan()

        elif choice == "6":
            break

        else:
            print(Color.RED + "Invalid option!\n" + Color.RESET)
