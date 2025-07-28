import pyttsx3
import random

engine = pyttsx3.init()

jokes = [
    "Why don't scientists trust atoms? Because they make up everything.",
    "I told my computer I needed a break, and it said 'No problem — I’ll go to sleep.'",
    "What do you call a fake noodle? An impasta!"
]

def run(_):
    joke = random.choice(jokes)
    engine.say(joke)
    engine.runAndWait()
    return joke

commands = ["tell me a joke", "joke", "make me laugh"]
