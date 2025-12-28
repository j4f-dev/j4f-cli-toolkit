from toolkit.banner import show_banner
from toolkit.system import system_info
from toolkit.network import network_info
from toolkit.utils import clear_screen, Color, slow_print
import sys


def main_menu():
    while True:
        print(Color.GREEN + "[1] System Info")
        print("[2] Network Info")
        print("[3] Clear Screen")
        print("[4] About Toolkit")
        print("[5] Exit" + Color.RESET)

        choice = input(Color.YELLOW + "\nj4f > " + Color.RESET)

        if choice == "1":
            system_info()

        elif choice == "2":
            network_info()

        elif choice == "3":
            clear_screen()
            show_banner()

        elif choice == "4":
            slow_print(Color.CYAN + "J4F CLI TOOLKIT — Built by Sohail")

        elif choice == "5":
            print(Color.RED + "Exiting...")
            sys.exit()

        else:
            print(Color.RED + "Invalid option!")


if __name__ == "__main__":
    show_banner()
    main_menu()
