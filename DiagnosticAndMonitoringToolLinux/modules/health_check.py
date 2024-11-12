import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return {"total": mem.total, "used": mem.used, "percent": mem.percent}

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return {"total": disk.total, "used": disk.used, "percent": disk.percent}

def get_network_usage():
    net_io = psutil.net_io_counters()
    return {"bytes_sent": net_io.bytes_sent, "bytes_recv": net_io.bytes_recv}

# Test each function
if __name__ == "__main__":
    print("CPU Usage:", get_cpu_usage(), "%")
    print("Memory Usage:", get_memory_usage())
    print("Disk Usage:", get_disk_usage())
    print("Network Usage:", get_network_usage())
