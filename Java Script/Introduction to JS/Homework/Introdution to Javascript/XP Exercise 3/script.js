while (true){
    let userAnswer = prompt("Type a number");
    let userNumber = parseInt(userAnswer); 

    if(isNaN(userNumber)){
        alert("Numbers ONLY");
    }
    
    if (userNumber >= 10){
        break;
    }
}

// Tried to use typeof but it didnt work as all


// while (true){
//     let userAnswer = prompt("Type a number");
//     if(typeof(userAnswer) != "number"){
//         alert("Numbers ONLY")
//         console.log(typeof(userAnswer));
//     }
//     if (userAnswer >= 10){
//         break;
//     }
// }