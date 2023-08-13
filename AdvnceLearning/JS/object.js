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