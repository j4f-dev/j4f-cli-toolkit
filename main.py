from toolkit.system import system_info
from toolkit.network import network_info
from toolkit.utils import clear_screen, Color, slow_print
import sys

def show_banner():
    clear_screen()
    print(Color.GREEN + Color.BOLD + r"""
 ██████╗ ██╗  ██╗███████╗
 ██╔══██╗██║  ██║██╔════╝
 ██████╔╝███████║█████╗  
 ██╔═══╝ ██╔══██║██╔══╝  
 ██║     ██║  ██║███████╗
 ╚═╝     ╚═╝  ╚═╝╚══════╝
    """ + Color.RESET)

    slow_print(Color.CYAN + "J4F CLI TOOLKIT — Built by Sohail\n" + Color.RESET)

def main_menu():
    while True:
        print(Color.GREEN + "[1] System Information")
        print("[2] Network Information")
        print("[3] Clear Screen")
        print("[4] Toolkit Info")
        print("[5] Exit" + Color.RESET)

        choice = input(Color.YELLOW + "\nj4f > " + Color.RESET)

        if choice == "1":
            system_info()
        elif choice == "2":
            network_info()
        elif choice == "3":
            show_banner()
        elif choice == "4":
            slow_print(Color.CYAN + "J4F CLI Toolkit | Version 1.0 | Developer: Sohail" + Color.RESET)
        elif choice == "5":
            print(Color.RED + "Exiting J4F Toolkit..." + Color.RESET)
            sys.exit()
        else:
            print(Color.RED + "Invalid option!" + Color.RESET)

if __name__ == "__main__":
    show_banner()
    main_menu()
