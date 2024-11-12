from modules.system_info import get_system_info
from modules.health_check import get_cpu_usage, get_memory_usage, get_disk_usage, get_network_usage
from modules.hardware_check import get_battery_status
from modules.report import save_report

def run_diagnostics():
    diagnostics = {
        "system_info": get_system_info(),
        "health_check": {
            "cpu_usage": get_cpu_usage(),
            "memory_usage": get_memory_usage(),
            "disk_usage": get_disk_usage(),
            "network_usage": get_network_usage()
        },
        "hardware_status": get_battery_status()
    }
    return diagnostics

if __name__ == "__main__":
    results = run_diagnostics()
    save_report(results)
    print("Diagnostics complete. Report saved to 'system_report.json'.")
