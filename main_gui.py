import tkinter as tk
from voice_engine import speak, listen
from search_module import google_search
from system_tasks import get_battery
from file_search import search_files
from plugin_manager import load_plugins

plugins = load_plugins()

def handle_command(cmd):
    cmd = cmd.lower()
    if "battery" in cmd:
        result = get_battery()
    elif "search file" in cmd:
        filename = cmd.split("search file")[-1].strip()
        found = search_files(filename)
        result = f"Found {len(found)} file(s)." if found else "No file found."
    elif cmd in plugins:
        result = plugins[cmd]()
    else:
        result = google_search(cmd)
    speak(result)
    return result

def run_gui():
    def on_click():
        query = listen()
        output = handle_command(query)
        result_var.set(output)

    app = tk.Tk()
    app.title("JARVIS PC")
    app.geometry("600x400")
    app.configure(bg="#0f172a")

    label = tk.Label(app, text="Ask JARVIS", font=("Helvetica", 20), fg="white", bg="#0f172a")
    label.pack(pady=20)

    tk.Button(app, text="Speak", command=on_click, font=("Arial", 14), bg="#10b981", fg="white", padx=20).pack()
    result_var = tk.StringVar()
    tk.Label(app, textvariable=result_var, font=("Arial", 14), fg="white", bg="#0f172a", wraplength=500).pack(pady=20)

    app.mainloop()

if __name__ == '__main__':
    run_gui()
