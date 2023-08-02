import pyttsx3
import datetime
import speech_recognition as sr # internet needed
from time import sleep
import math_calc, joke


engine =pyttsx3.init() #Ava
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.setProperty('rate', 143)
engine.setProperty('word_rate', 150)
engine.setProperty('volume', 0.9)
engine.setProperty('pitch', 100)
engine.setProperty('age', 'young')
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
        hr =datetime.datetime.now().hour
        if 5 <= hr < 12:
            return 'Morning'
        elif 12 <= hr < 18:
            return 'Afternoon'
        elif 18 <= hr < 22:
            return 'Evening'
        else:
            return 'Night'
    speak(f'Welcome back')
    speak(time())
    speak(date())
    speak(f'Good {wishTime()}, I am Ava. how can I be of service')

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

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'shutdown' in query:
            speak("Have a nice day. bye...")
            break
        if 'calculate' in query:
            answer = str(math_calc.calculate(query))
            print(f'{query} = {answer}')
            speak(f'{query} = {answer}')
        if 'joke' in query:
            c = 'yes'
            while c == 'yes':
                joke = joke.tellMeJoke()
                speak(joke)
                print(joke)
                sleep(3)
                speak('Do you want to tell me another joke')
                print('Do you want to tell me another joke')
                c = takeCommand().lower()
            else:
                print('i hope you enjoyed my jokes')
                speak('i hope you enjoyed my jokes')