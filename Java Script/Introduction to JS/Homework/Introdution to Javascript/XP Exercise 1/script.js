const people = ["Greg", "Mary", "Devon", "James"];

people.shift();
console.log(people)

let jamesIndex = people.indexOf("James");
people[jamesIndex] = "Jason";

// let lastIndex = people.length - 1;
// people[lastIndex] = "Jason";
// console.log(people[lastIndex]);

people.push("Alex");
console.log(people);

let maryIndex = people.indexOf("Mary");
console.log(maryIndex);

let alexIndex = people.indexOf("Alex");
let peopleCopy = people.slice(maryIndex + 1, alexIndex);
console.log(peopleCopy);

let fooIndex = people.indexOf("Foo");
console.log(fooIndex);
// returns -1 because Foo is not in array

let lastIndex = people.length - 1;
let last = people[lastIndex];
console.log(last);

for(let i = 0; i < people.length; i++){
    console.log(people[i]);
}

// let devonIndex = people.indexOf("Devon");
// for(let i = 0; i < people.length; i++){
//     if(i == devonIndex){
//         break;
//     }
//     console.log(people[i]);
// }


for(let i = 0; i < people.length; i++){
    let person = people[i];
    if (person == "Devon") {
        console.log(person);
        break;
    }
}