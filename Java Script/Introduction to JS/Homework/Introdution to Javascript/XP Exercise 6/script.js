const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'reindeer'
  }

let sentence = "";
for (let detail in details ){
   
    sentence = sentence + detail + " " + details[detail] + " ";
}

console.log(sentence);