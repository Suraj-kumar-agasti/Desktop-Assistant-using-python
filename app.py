from src.helper import speak,takecommand , wish_me
import datetime
import wikipedia
import webbrowser
import os

if __name__ == "__main__":
    wish_me()

    while True:
        query = takecommand().lower()
    
        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "google" in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif "github" in query:
            speak("opening github")
            webbrowser.open("github.com")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif "good bye" in query:
            speak("ok sir. I am always here for you. bye bye")
            exit()










