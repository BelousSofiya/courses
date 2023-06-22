// Task02 - you are given a string which contains multiple numbers (integer and floating points).
// Your task is to extract all numbers from a string and return them in an array in such order as they are met in a string.
// Dot (".") is used as a separator between integer and decimal portion of the nubmer.
// Numbers that are used as part of a word should also be extracted (like 2nd or 3rd).
// Return 'null' if string has no numbers
// Sample:
// inputString: "Hello 2.15 digital World 5,3"
// Result array of 3 elements: [2.15, 5, 3]

function task02(inputString) {
    // TODO: Write your code here
    //let re = /(\d+\.?\d+)|\d+/g;   it works too
    let re = /\d+(\.\d+)?/g;
    if(inputString.match(re)){return inputString.match(re)}else{return 'null'};
}
console.log(task02("Hello 2.15 digital World 5,3"))