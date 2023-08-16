import datetime
WISH_WORDS = ["hello", "hi", "hey", "howdy", "good morning", "good afternoon", "good evening", "greetings", "salutations", "hey there", "yo", "what's up", "hiya", "sup", "hola", "namaste", "bonjour", "good day", "hello there", "hi there"]
GREETINGS_SENTENCES = ["how are you", "how's it going", "how have you been", "how do you do", "what's up", "what's going on", "how are things", "how's life", "how are you doing", "howdy", "how are ya", "what's happening", "what's new", "how's your day", "how's everything", "how's your day going", "how are you today", "how are you holding up", "how's your week", "how are you feeling"]
TIME_SENTENCES = ["current time", "what's the time", "tell me the time", "time please", "what time is it", "what's the current time", "can you tell me the time", "do you know the time", "what is the time now", "time", "tell me time", "what time do we have", "do you have the time"]
DATE_SENTENCES = ["current date", "what's the date", "tell me the date", "date please", "what is today's date", "what's the current date", "can you tell me the date", "do you know the date", "today's date", "tell me date", "what date is it", "do you have the date", "what's today's date", "do you know today's date"]
NAME_SENTENCES = ["what is your name", "who are you", "tell me your name", "what's your name", "may I know your name", "who is this", "what do I call you", "your name please", "who are you?", "who's speaking", "what should I call you", "what can I call you", "do you have a name", "identify yourself"]
CAPABILITIES_SENTENCES = ["what can you do",'tell me about yourself', "what are your abilities", "tell me your capabilities", "what are you capable of", "what functionalities do you have", "what tasks can you perform", "what do you know how to do", "what are your skills", "list your abilities", "what are your features", "what tasks are you designed for", "what services can you provide", "what do you offer", "what are your functions"]
ADULT_CONTENT_WORDS = ['adult material', 'bare-skinned', 'sexual content', 'uncovered', '18+', 'sexy', 'nudity', 'adult theme', 'bare', 'adults-only', 'obscene', 'disrobed', 'nsfw', 'stripped', 'streaking', 'porn', 'sexual', 'sexually explicit', 'sex', 'unclothed', 'topless', 'indecent exposure', 'pornography', 'vulgar', 'mature content', 'sexually-oriented', 'intimate', 'explicit', 'mature', 'adult', 'erotic', 'nude', 'lewd', 'sensual', 'xxx', 'exposed', 'bottomless', 'raunchy', 'adult content', 'undressed', 'risqué', 'naked', 'indecent', 'provocative']
def greeting_sentence(greeting):
    if "how" in greeting and "you" in greeting:
        return "I'm just a computer program, but I'm doing fine. Thank you for asking!"
    elif "what's up" in greeting or "what's going on" in greeting or "what's happening" in greeting or "what's new" in greeting:
        return "Not much, just here to assist you!"
    elif "how are things" in greeting or "how's life" in greeting:
        return "I'm an AI, so I don't have feelings, but I'm ready to help you!"
    elif "how do you do" in greeting:
        return "I'm doing well, thank you. How can I assist you?"

def basicConversation(user_input):
    if any(user_input.startswith(word) for word in WISH_WORDS):
        return 'Hello! How can I help you?'
    elif user_input in GREETINGS_SENTENCES:
        return greeting_sentence(user_input)
    elif user_input in TIME_SENTENCES:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"current time is: {current_time}"
    elif user_input in DATE_SENTENCES:
        current_date = datetime.date.today()
        return f"current date is: {current_date}"
    elif user_input in NAME_SENTENCES:
        return "My name is Ava created by Sarath and I'm your virtual assistant"
    elif user_input in CAPABILITIES_SENTENCES:
        return "Currently, I can perform arithmetic operations and share jokes with you. If you have any questions or need assistance, feel free to ask!"
    elif user_input in ADULT_CONTENT_WORDS:
        return "I am sorry to share such a rude info"
    else:
        return ""

# if __name__ == "__main__":
#     #print(basicConversation(input(":")))