import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# taking voice from my system
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
print(voices[0].id)
# print(type(voices))
engine.setProperty('voice',voices[1])
engine.setProperty('rate',180)

# speak function 

def speak(text):
    """ This function takes text and returns voice
    Args:
         text(__type__): string
    """

    engine.say(text)
    engine.runAndWait()


# speech recognition
def takecommand():
    """This function will recognize voice and return text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "none"
        return query
    
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good morning sir. How are you doing")
    elif hour>12 and hour<18:
        speak("Good afternoon sir. How are you doing")
    else:
        speak("Good evening sir. How are you doing")
    speak("I am Jarvis. Tell mehow can I help you ?")

    