// Create an array to store login emails
var loginEmails = [];

// Function to handle form submission
function submitForm(event) {
    event.preventDefault(); // Prevent form from submitting
    // Get the input value from the email field
    var inputEmail = document.getElementById("email").value;

    if (inputEmail == ""){
        alert("Fill the box with your outlook");
    }// Check if the input email is already in the loginEmails array
     else if (loginEmails.includes(inputEmail)) {
        alert("Successfully logged in");
    } else {
        // Add the input email to the loginEmails array
        loginEmails.push(inputEmail);
        alert("Successfully registered and logged in");
    }
}

// Add event listener to the form for submission
var form = document.getElementById("loginForm");
form.addEventListener("submit", submitForm);