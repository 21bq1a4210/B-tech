function demoSetTimeout(){
    let sum =0;
    for (let i=1; i<=5; i++){
        sum += i;
        setTimeout( () => {
            console.log(`Delayed for ${i} second`);
        }, sum*1000);
    } 
}

function asynchronous(){
    setTimeout(() => {
        console.log("this is the first message");
      }, 5000);
      setTimeout(() => {
        console.log("this is the second message");
      }, 3000);
      setTimeout(() => {
        console.log("this is the third message");
      }, 1000);
      
      // Output:
      
      // this is the third message
      // this is the second message
      // this is the first message      
}