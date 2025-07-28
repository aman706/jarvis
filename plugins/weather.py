import requests
import pyttsx3

engine = pyttsx3.init()

def run(location="delhi"):
    try:
        url = f"https://wttr.in/{location}?format=3"
        res = requests.get(url)
        weather = res.text
        engine.say(weather)
        engine.runAndWait()
        return weather
    except Exception as e:
        return f"Error: {e}"

commands = ["weather", "what's the weather", "temperature"]
