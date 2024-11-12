import json
from datetime import datetime

def save_report(data, filename="system_report.json"):
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# Example usage
if __name__ == "__main__":
    sample_data = {
        "system_info": {"OS": "Linux", "CPU": "Intel i7"},
        "health_check": {"cpu_usage": 15, "memory_usage": {"total": 8, "used": 4}}
    }
    save_report(sample_data)