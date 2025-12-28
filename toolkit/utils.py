import os

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

def banner():
    clear_screen()
    print("""
███████╗██╗  ██╗███████╗
██╔════╝██║  ██║██╔════╝
█████╗  ███████║█████╗
██╔══╝  ██╔══██║██╔══╝
███████╗██║  ██║███████╗

j4f-cli-toolkit
""")
