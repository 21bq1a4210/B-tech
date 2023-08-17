let iterations = 10;
function run(){
    const number = parseInt(document.getElementById("number").value);
    const tbBody = document.getElementById("mulTable");
    tbBody.innerHTML = '';
    for (let last=1; last<=iterations; last++){
        setTimeout(() =>{
            const tbRow = tbBody.insertRow();
            tbRow.insertCell().textContent = number;
            tbRow.insertCell().textContent = "*"
            tbRow.insertCell().textContent = last;
            tbRow.insertCell().textContent = "=";
            tbRow.insertCell().textContent = number*last;
        },last*1000 );
    }
}

document.querySelector("#run").addEventListener("click", run);