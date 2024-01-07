function dragStart(ev) {
    ev.dataTransfer.effectAllowed = 'move';
    ev.dataTransfer.setData("Text", ev.target.getAttribute('id'));
    ev.dataTransfer.setDragImage(ev.target, 0, 0);
    return true;
}

function dragEnter(ev) {
    ev.preventDefault();
    return true;
}

function dragOver(ev) {
    return false;
}

function dragDrop(ev) {
    var scr = ev.dataTransfer.getData('Text');
    ev.target.appendChild(document.getElementById(scr));
    ev.stopPropagation();
    return false;
}
