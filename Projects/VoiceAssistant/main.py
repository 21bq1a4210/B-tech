import pyttsx3
import datetime

engine =pyttsx3.init() #Ava
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.setProperty('rate', 143)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    tim = datetime.datetime.now().strftime("%I:%M")
    return f"The current time is: {tim}"

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    return (f"The current date is: {date} {month} {year}")

def wishMe():
    def wishTime():
        hr = int(datetime.datetime.now().strftime('%I'))
        if 5 <= hr >= 11:
            return 'Morning'
        elif 12 <= hr >= 17:
            return 'afternoon'
        elif 18 <= hr >= 22:
            return 'evening'
        else:
            return 'night'
    speak(f'Good {wishTime()}. Welcome back')
    speak(time())
    speak(date())
    speak('Hello there, I am Ava. how can I be of service')
wishMe()