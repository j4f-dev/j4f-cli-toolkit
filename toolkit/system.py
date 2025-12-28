import platform

def system_info():
    print("\n--- System Information ---")
    print("OS       :", platform.system())
    print("Release  :", platform.release())
    print("Version  :", platform.version())
    print("Machine  :", platform.machine())
    print("Processor:", platform.processor())
