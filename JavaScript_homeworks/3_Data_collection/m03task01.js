// Task01 - create a function with name task01
// function pass three numbers and multiples those that less than zero
// if all numbers are positive function should return undefined
// for example: 
// if function take 3, -2 and -5 it should return 10

// TODO: Define your function here
function task01(a, b, c){
    let i = 1;
    let arr = [a, b, c];
    for(e=0; e<arr.length; e++){
        i *= (arr[e]<0)? arr[e]:1
}
    console.log(i);
}

task01(3, -2, -5);