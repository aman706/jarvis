import psutil
import os
import webbrowser

def get_battery():
    battery = psutil.sensors_battery()
    return f"Battery: {battery.percent}% {'(Charging)' if battery.power_plugged else ''}"

def open_app(path):
    os.startfile(path)

def open_website(url):
    webbrowser.open(url)
