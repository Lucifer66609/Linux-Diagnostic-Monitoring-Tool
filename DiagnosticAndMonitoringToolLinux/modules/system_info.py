import platform
import psutil
import socket

def get_system_info():
    # General system information
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Hostname": platform.node(),
        "CPU": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=True),
        "Memory (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
    }
    
    # Network information - Selects the first active, non-loopback interface
    for interface_name, interface_addresses in psutil.net_if_addrs().items():
        for address in interface_addresses:
            if address.family == socket.AF_INET and interface_name != "lo":
                info["IP Address"] = address.address
                break
        if "IP Address" in info:
            break
    
    return info

# Test the function
if __name__ == "__main__":
    for key, value in get_system_info().items():
        print(f"{key}: {value}")