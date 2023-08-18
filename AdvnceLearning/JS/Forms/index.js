const form = document.getElementById("userForm");

form.addEventListener("submit", function(event){
    event.preventDefault();
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("pasword").value;
    const date = document.getElementById("date").value;
    const csvData = `"Name","Email","Password","Date"\n"${name}","${email}","${password}","${date}"`;
    console.log("CSV Data:", csvData);
});
// import "./fs";
// console.log(FileSystem)