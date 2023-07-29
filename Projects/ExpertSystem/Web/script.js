// Get the elements
const chatOutput = document.getElementById('chat-output');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-btn');

// Event listener for the send button
sendButton.addEventListener('click', sendMessage);

// Event listener for pressing the Enter key in the message input
messageInput.addEventListener('keypress', function (event) {
  if (event.key === 'Enter') {
    sendMessage();
  }
});

// Function to send a new message
function sendMessage() {
  const message = messageInput.value.trim();

  if (message !== '') {
    appendMessage('You', message);
    messageInput.value = '';
  }
}

// Function to append a new message to the chat output
function appendMessage(sender, message) {
  const messageElement = document.createElement('div');
  messageElement.classList.add('message');

  const senderElement = document.createElement('span');
  senderElement.classList.add('sender');
  senderElement.textContent = sender + ': ';

  const textElement = document.createElement('span');
  textElement.textContent = message;

  messageElement.appendChild(senderElement);
  messageElement.appendChild(textElement);

  chatOutput.appendChild(messageElement);

  // Scroll to the bottom of the chat output
  chatOutput.scrollTop = chatOutput.scrollHeight;
}
