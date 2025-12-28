import socket
from toolkit.utils import Color

def advanced_port_scan():
    target = input(Color.YELLOW + "Enter domain or IP: " + Color.RESET)

    try:
        start_port = int(input(Color.YELLOW + "Start port: " + Color.RESET))
        end_port = int(input(Color.YELLOW + "End port: " + Color.RESET))

        target_ip = socket.gethostbyname(target)
        print(Color.CYAN + f"\nScanning {target} ({target_ip}) ports {start_port}-{end_port}\n" + Color.RESET)

        open_ports = []

        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)

            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
                print(Color.GREEN + f"[OPEN] Port {port}")

            sock.close()

        if not open_ports:
            print(Color.RED + "\nNo open ports found.")

        else:
            print(Color.CYAN + f"\nOpen ports: {open_ports}")

        print(Color.RESET)

    except ValueError:
        print(Color.RED + "Invalid port number!" + Color.RESET)

    except socket.gaierror:
        print(Color.RED + "Invalid domain or IP!" + Color.RESET)
