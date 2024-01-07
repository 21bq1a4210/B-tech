function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text/html", ev.target.id);
}

function drop(ev) {
    ev.preventDefault(); // Prevent the default behavior of the drop event
    var data = ev.dataTransfer.getData("text/html"); // Fix the typo in 'text/hmtl'
    ev.target.appendChild(document.getElementById(data));
}
