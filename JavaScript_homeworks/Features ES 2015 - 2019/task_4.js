//The function takes any number of strings and returns the sum of their lengths.
//Example:
//console.log(sumOfLen('hello', 'hi')); //7
//console.log(sumOfLen('hi')); //2
//console.log(sumOfLen()); //0
//console.log(sumOfLen('hello', 'hi', 'my name', 'is')); //16

const sumOfLen = (...strings) => {
    const sum = strings.reduce(
  (accumulator, currentValue) => accumulator + currentValue.length, 0);
  return sum;
};

console.log(sumOfLen('hello', 'hi'));//Expect 7

console.log(sumOfLen('hi'));//Expect 2

console.log(sumOfLen());//Expect 0

console.log(sumOfLen('hello', 'hi', 'my name', 'is'));//Expect 16

console.log(sumOfLen('hello', 'hi', 'my name', 'is2'));//Expect 17

console.log(sumOfLen('hello', 'my name', 'is'));//Expect 14

console.log(sumOfLen('hello', 'my name'));//Expect 12