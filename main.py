"""
j4f-cli-toolkit
Author: Sohail
Description: A clean and professional Python CLI toolkit.
"""

import sys
from toolkit.system import system_info, clear_screen


def show_banner():
    clear_screen()
    print("""
====================================
        j4f-cli-toolkit
====================================
A Professional Python CLI Toolkit
""")


def show_help():
    print("""
Available Commands
------------------
info    Show system information
clear   Clear the screen
help    Show this help menu
exit    Exit the toolkit
""")


def main():
    show_banner()

    while True:
        command = input("j4f > ").strip().lower()

        if command == "info":
            system_info()
        elif command == "clear":
            show_banner()
        elif command == "help":
            show_help()
        elif command == "exit":
            print("Exiting j4f-cli-toolkit...")
            sys.exit(0)
        else:
            print("Unknown command. Type 'help' to see available commands.")


if __name__ == "__main__":
    main()
