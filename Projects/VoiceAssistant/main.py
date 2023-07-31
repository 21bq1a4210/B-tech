import pyttsx3
import datetime
import speech_recognition as sr # internet needed

engine =pyttsx3.init() #Ava
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.setProperty('rate', 143)
def speak(audio):
    '''
    the function is used to speak the audio
    :param audio: a str which need to be speaking
    '''
    engine.say(audio)
    engine.runAndWait()
def time():
    '''
    this function is used to calculate the current time
    :return: time in hr:min
    '''
    tim = datetime.datetime.now().strftime("%I:%M")
    return f"The current time is: {tim}"

def date():
    '''
    this function is used to calculate the current date
    :return: date:month:year
    '''
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    return f"The current date is: {date} {month} {year}"

def wishMe():
    '''
    This function will wish the customer
    :return:
    '''
    def wishTime():
        '''
        This function will determine the wishing time
        :return: greetings
        '''
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

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return 'None'
    return query

takeCommand()
