let timeoutID;
let text = document.getElementById("txt");
function setOutput(outputContent) {
  document.querySelector("#output").textContent = outputContent;
}

function delayedMessage() {
  setOutput("Wait 2 sec");
  timeoutID = setTimeout(setOutput, 2 * 1000, text.value);
}

function clearMessage() {
    setOutput("");
    clearTimeout(timeoutID);
}
