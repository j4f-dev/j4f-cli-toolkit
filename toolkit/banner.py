import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

def slow_print(text, delay=0.002):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_banner():
    banner = f"""
{Fore.CYAN}
     ██╗ ██╗  ███████╗
     ██║ ██║  ██╔════╝
     ██║ ██║  █████╗
██   ██║ ██║  ██╔══╝
╚█████╔╝ ██║  ██║
 ╚════╝  ╚═╝  ╚═╝

{Fore.GREEN}      J4F CLI TOOLKIT
{Fore.YELLOW}  Fast • Clean • Hacker Style
{Fore.MAGENTA}  github.com/j4f-dev/j4f-cli-toolkit
{Style.RESET_ALL}
"""
    slow_print(banner)
