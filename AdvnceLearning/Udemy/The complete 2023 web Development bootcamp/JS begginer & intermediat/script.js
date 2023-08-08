function getBMI(wt,ht){
    return wt/(ht*ht);
}

//random int gen
function diesChoose(){
    var n = Math.floor(Math.random()*6)+1;
    console.log(n)
}

//Conditional statements
function leapYear(year){
    if ((year%4==0 && year%100!=0)||(year%400==0)){
        console.log("leapYear");
    } else {
        console.log("non leapYear");
    }
}

//Arrays:
function invitation(){
    var gList = ["A", "B", "C", "D"];
    var gust = prompt("Enter your name:");
    if(gList.includes(gust)){
        alert("Welcome "+gust);
    } else {
        alert("you are not allowed here");
    }
}

//Adding elements to the array and while:
var output = [];
count = 1;

function fizzBuzz(){
    while (count <= 100){
        if (count%3 == 0 && count%5 == 0){
        output.push("FizzBuzz");
        }else if (count%5==0){
            output.push("Buzz");
        }else if (count%3==0){
            output.push("fizz");
        }else{
            output.push(count);
        } 
        count++;
        console.log(output);
    }
} 