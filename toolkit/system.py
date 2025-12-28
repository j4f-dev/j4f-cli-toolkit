"""
System utilities for j4f-cli-toolkit
"""

import os
import platform


def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")


def system_info():
    print("\nSystem Information")
    print("------------------")
    print(f"OS        : {platform.system()}")
    print(f"Release   : {platform.release()}")
    print(f"Machine   : {platform.machine()}")
    print(f"Python    : {platform.python_version()}")
