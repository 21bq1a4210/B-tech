// object methosds in js 
// Everything you need to master Object in Js 

// 1.
// Object.create()
// Object.keys()
// Object.values()

// 2.
// Object.entries()
// Object.assign()
// Object.freeze()

// 3.
// Object.seal()
// Object.getPrototypeOf()
// Object.setPrototypeOf()


// Object.create() :
// The Object.create() method is used to create a 
// new object and link it to the prototype of an 
// existing object. We can create a job object 
// instance, and extend it to a more specific object.
const job = {
    position: "cashier",
    type:"hourly",
    isAvailable:true,
    showDetails() {
        const accepting = this.isAvailable ? "is open" : "is closed"
        console.log(
            `The ${this.position} position is ${this.type} and ${accepting}.`
        )
    },
}
// Use Object.create to pass properties
const barista = Object.create(job);
barista.position = "barista";
barista.showDetails();
// Output:
// The barista position is hourly and is open.


// Object.keys() :
// Object.keys() creates an array containing the keys of an object. 
// We can  create an object and print the array of keys.

// Initialize an object
const employees = {
    boss: "Sarath",
    secretary: "Chandra",
    sales: "Mij",
    accountant: 'Gmo'
};
// Get the keys of the object
const keys = Object.keys(employees);
console.log(keys);
// Output:
// ['boss', 'secretary', 'sales', 'accountant']


// Object.values() :
// Object.values() create an array containing the
// values of an object

// Initialize an object
const session = {
    id: 1,
    time: "26-July-2023",
    device: "mobile",
    browser: "Brave"
};
// Get all values of the object 
const values = Object.values(session);
console.log(values);
// Output:
// [1, '26-July-2023', 'mobile', 'Brave']


// Object.entries() :
// Object.entries() creates a nested array of the 
// key/value pairs of an Object

// Initialize an object 
const OS = {
    name: "Ubuntu",
    version: 22.04,
    license: "Open Source"
};
// Get the Object key/value pairs 
const entries = Object.entries(OS);
console.log(entries);
// Output:
// [Array(2), Array(2), Array(2)]
// 0
// : 
// (2) ['name', 'Ubuntu']
// 1
// : 
// (2) ['version', 22.04]
// 2
// : 
// (2) ['license', 'Open Source']


// Object.assign() :
// Object.assign is used to copy values from one Object
// to another, we can create 2 objects, and merge 
// them with objects.assign(). 

// Initialize an object 
const name = {
    firstName: "Sarath",
    lastName: "chandra"
};
// Initialize another object 
const details = {
    job: "student",
    college: "VVIT"
};
// Merge the objects
const char = Object.assign(name, details);
console.log(char);
// Output:
// {firstName: 'Sarath', lastName: 'chandra', job: 'student', college: 'VVIT'}


// Object.freeze() :
// Object.freeze() prevents modification to properties
// and values of an object and prevents properties
// from being added or removed from an object.

// Initialize an object 
const user = {
    username: "asdfg",
    password:"12eds"
};
// Freeze the object
const newUser = Object.freeze(user);

newUser.password = "**********";
newUser.active = true;
console.log(newUser);
// Output:
// {username: 'asdfg', password: '12eds'}