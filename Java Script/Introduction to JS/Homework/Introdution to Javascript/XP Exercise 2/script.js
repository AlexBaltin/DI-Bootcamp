let colors = ["black", "white", "green", "blue"]
let suffixes = ["st", "nd", "rd", "th"]
console.log(colors);

for(let i = 0; i < colors.length; i++){
    console.log("My #"+(i+1)+" choice is "+colors[i])
}

for(let i = 0; i < colors.length; i++){
    console.log("My "+(i+1)+suffixes[i]+" choice is "+colors[i])
}