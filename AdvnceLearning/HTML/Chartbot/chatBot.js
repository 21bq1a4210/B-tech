// Send the user's input to Dialogflow and receive the chatbot's response
function sendMessage() {
    let userMessage = document.querySelector("#user-input").value;
    let chatContent = document.querySelector("#chat-content");
    chatContent.innerHTML += "<p>User: " + userMessage + "</p>";
    // Make an HTTP request to the Dialogflow API
    fetch("https://api.dialogflow.com/v1/query?v=20150910", {
      method: "POST",
      headers: {
        "Authorization": "Bearer <Your Dialogflow API Key>",
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        query: userMessage,
        lang: "en",
        sessionId: "12345"
      })
    })
    .then(response => response.json())
    .then(data => {
      chatContent.innerHTML += "<p>Chatbot:
  