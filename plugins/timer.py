import time
import pyttsx3

engine = pyttsx3.init()

def run(command):
    words = command.split()
    try:
        seconds = int([w for w in words if w.isdigit()][0])
        engine.say(f"Starting timer for {seconds} seconds")
        engine.runAndWait()
        time.sleep(seconds)
        engine.say("Time's up!")
        engine.runAndWait()
        return "Timer complete."
    except:
        return "Couldn't understand the duration."

commands = ["set timer", "start timer", "countdown"]
