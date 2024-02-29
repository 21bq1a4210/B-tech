// Sample JavaScript code for handling patient data
let patients = [];

function addPatient() {
    const name = document.getElementById('patient-name').value;
    const age = document.getElementById('patient-age').value;
    const gender = document.getElementById('patient-gender').value;

    const newPatient = { name, age, gender };
    patients.push(newPatient);

    displayPatients();
    clearForm();
}

function displayPatients() {
    const patientListUl = document.getElementById('patient-list-ul');
    patientListUl.innerHTML = '';

    patients.forEach(patient => {
        const li = document.createElement('li');
        li.textContent = `${patient.name} - ${patient.age} years old (${patient.gender})`;
        patientListUl.appendChild(li);
    });
}

function clearForm() {
    document.getElementById('add-patient-form').reset();
}

// Initially display any existing patients
displayPatients();
