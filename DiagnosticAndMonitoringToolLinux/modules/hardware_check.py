import psutil

def get_battery_status():
    battery = psutil.sensors_battery()
    if battery:
        return {
            "percent": battery.percent,
            "plugged_in": battery.power_plugged
        }
    else:
        return "No battery detected"

# Test the function
if __name__ == "__main__":
    print("Battery Status:", get_battery_status())
