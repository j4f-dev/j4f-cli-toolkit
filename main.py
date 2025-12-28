from toolkit.system import system_info
from toolkit.network import network_info
from toolkit.utils import clear_screen
import sys

def banner():
    clear_screen()
    print("""
    ██████╗ ██╗  ██╗███████╗
    ██╔══██╗██║  ██║██╔════╝
    ██████╔╝███████║█████╗
    ██╔═══╝ ██╔══██║██╔══╝
    ██║     ██║  ██║███████╗
    ╚═╝     ╚═╝  ╚═╝╚══════╝

        J4F CLI TOOLKIT
    """)

def menu():
    while True:
        print("""
[1] System Information
[2] Network Information
[3] Clear Screen
[4] Toolkit Info
[5] Exit
""")
        choice = input("j4f > ")

        if choice == "1":
            system_info()
        elif choice == "2":
            network_info()
        elif choice == "3":
            banner()
        elif choice == "4":
            print("\nJ4F CLI Toolkit\nBuilt for learning & automation")
        elif choice == "5":
            print("👋 Exiting J4F CLI Toolkit")
            sys.exit()
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    banner()
    menu()
