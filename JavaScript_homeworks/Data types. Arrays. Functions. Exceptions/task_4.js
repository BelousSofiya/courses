//Implement the processArray(arr, factorial) function, which takes the first parameter of the array arr, and the second
//parameter the function factorial and processes each element of the array arr with the function factorial, returning
//a new array (the source array arr does not change)
//The function factorial(n) calculates and returns the factorial of the number n. For example factorial(4) returns 24.
//Example
//// determines the factorial of the number n
//function factorial(n) { // your code};
//processArray([1, 2, 3, 4, 5], factorial); // [1, 2, 6, 24, 120]

function factorial(n) {
    if(n < 0){
        return "number has to be positive."
    }
    if(n == 0 || n == 1){
        return 1;
    }else{
        return n * factorial(n-1);
    }
}

function processArray(arr, factorial) {
    let result = arr.reduce((total, amount) => {
        return total.concat(factorial(amount));
        }, []);
    return result;
    }

//Tests

console.log(processArray([1, 2, 3, 4, 5, 6], factorial));
//Expect [ 1, 2, 6, 24, 120, 720 ]

console.log(processArray([6, 5, 4, 3, 2, 1], factorial));
//Expect [ 720, 120, 24, 6, 2, 1 ]

console.log(processArray([0, 9, 4, 12], factorial));
//Expect [ 1, 362880, 24, 479001600 ]

console.log(processArray([9, 8, 13, 22], factorial));
//Expect [ 362880, 40320, 6227020800, 1.1240007277776077e+21 ]

console.log(processArray([], factorial));
//Expect []

const arr = [2, 4, 6];
console.log(processArray(arr, factorial));
console.log(arr);
//Expect [ 2, 24, 720 ]
//       [ 2, 4, 6 ]