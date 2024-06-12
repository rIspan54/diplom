import speech_recognition as sr

def record_volume():
    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)

    query = r.recognize_google(audio, language = "ru-RU")
    
    return query
