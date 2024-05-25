import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS


GOOGLE_API_KEY = "AIzaSyD-rmJUxW-bkhTMRPL5JVF_1gNhNaOpT9k"

os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

# speech recognition
def voice_input():
    """This function will recognize voice and return text."""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("you said",text)
            return text
            
        except sr.UnknownValueError:
            print("Sorry, could not understand audio")
        except sr.RequestError as e:
            print("Could not request from google speech Recognition service;{0}".format(e))

def text_to_speech(text):
    # create a gTTS object
    tts = gTTS(text = text, lang = 'en') # language can be changed

    # Save the audio as an MP3 file
    tts.save("speech.mp3")

def llm_model_object(user_text):
    genai.config(api_key = GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_text)
    result = response.text
    return result


