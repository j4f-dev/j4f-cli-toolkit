import socket
from toolkit.utils import Color

def port_scan():
    target = input(Color.YELLOW + "Enter domain or IP: " + Color.RESET)

    try:
        target_ip = socket.gethostbyname(target)
        print(Color.CYAN + f"\nScanning {target} ({target_ip})...\n" + Color.RESET)

        common_ports = {
            21: "FTP",
            22: "SSH",
            23: "TELNET",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            143: "IMAP",
            443: "HTTPS",
            3306: "MySQL",
            8080: "HTTP-ALT"
        }

        open_ports = False

        for port, service in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(Color.GREEN + f"[OPEN] Port {port} ({service})")
                open_ports = True

            sock.close()

        if not open_ports:
            print(Color.RED + "No common open ports found.")

        print(Color.RESET)

    except socket.gaierror:
        print(Color.RED + "Invalid domain or IP!" + Color.RESET)
