import pyttsx3

def audio(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()