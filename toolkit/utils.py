import os
import platform

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def os_info():
    return {
        "OS": platform.system(),
        "Version": platform.version(),
        "Architecture": platform.machine(),
        "Python": platform.python_version()
    }
