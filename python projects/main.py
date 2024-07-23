import speech_recognition as sr
import pyttsx3 as tts
import os
import random
import subprocess
import psutil

# Initialize the text-to-speech engine
engine = tts.init()
def say(speak):
    engine.say(speak)
    engine.runAndWait()

def recognize():
    rec = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        
        try:
            audio = rec.listen(source, timeout=10, phrase_time_limit=10)
            word = rec.recognize_google(audio)
            print(word)
            return word.lower()
        
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return ""
        
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""

result = recognize()

if result == "hello":
    say("hi sooraj")

if result == "how are you":
    say("doing great sir. how about you")
    
if result == "what is your name":
    say("my name is vocalisyn")

if result == "open notepad":
    say("opening notepad")
    os.system('notepad')
    
if result == "shutdown this system":
    say("closing all windows")
    say("shutting down")
    os.system('shutdown /s /t 1')
