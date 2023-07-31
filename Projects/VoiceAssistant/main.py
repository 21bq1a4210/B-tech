import pyttsx3
import datetime

engine =pyttsx3.init() #Ava
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.setProperty('rate', 135)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    tim = datetime.datetime.now().strftime("%I:%M:%S")
    speak(tim)
time()