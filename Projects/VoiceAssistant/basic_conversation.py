import datetime
def basicConversation(user_input):
    if 'hello' or 'hi' in user_input:
        return 'Hello! How can I help you?'
    elif 'how are you' in user_input:
        return "I'm just a computer program, but I'm doing fine. Thank you for asking!"
    elif 'current time' or 'time':
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"current time is: {current_time}"
    elif 'current date' or 'date':
        current_date = datetime.date.today()
        return f"current date is: {current_date}"

