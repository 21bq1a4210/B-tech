from django.shortcuts import render
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def chat(request):
    if request.method == 'POST':
        try:
            # Extract user message from request (e.g., form submission)
            user_message = request.POST.get('message')

            # Send user message to Rasa API
            url = "http://localhost:5005/webhooks/rest/webhook"
            data = {"sender": "user", "message": user_message}
            response = requests.post(url, json=data)

            # Check if response is successful
            if response.status_code == 200:
                # Process the Rasa response
                rasa_response = response.json()

                # Check if response contains data
                if rasa_response:
                    chatbot_response = rasa_response[0]
                else:
                    chatbot_response = "Sorry, I couldn't understand that."

                # Render the chatbot response in the template
                context = {'chatbot_response': chatbot_response}
                return render(request, 'chatbot.html', context)
            else:
                logger.error(f"Failed to get response from Rasa server. Status code: {response.status_code}")
                return render(request, 'chatbot.html', {'error_message': 'Failed to get response from Rasa server. Please try again later.'})
        except Exception as e:
            logger.exception("An error occurred while processing the request.")
            return render(request, 'chatbot.html', {'error_message': 'An error occurred. Please try again later.'})
    else:
        return render(request, 'chatbot.html')
