import pyttsx3

engine =pyttsx3.init() #Ava
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.setProperty('rate', 135)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak('Hey, hi i am Ava your Ai Assistant')
