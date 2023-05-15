//Implement the modifyArray(array) function, which takes an arbitrary array, changes the value of the first element of
//the array to “Start”, the last element of the array to “End” and returns the modified array.
//Function example:
//modifyArray([12, 6, 22, 0, -8])); // [‘Start’, 6, 22, 0, ‘End’]

function modifyArray(array) {
   array[0] = "Start";
   array[array.length-1] = "End";
   return array;
}

//Tests

const expected = ['Start', 6, 22, 0, 'End'];
const actual = modifyArray([12, 6, 22, 0, -8]);
console.log(actual.length === expected.length &&
  actual.every((value, key) => value === expected[key]));
//console.log(modifyArray([12, 6, 22, 0, -8]));
// Expect true

const expected = [ 'Start', 'Peter', 'Mark', 'End' ];
const actual = modifyArray(["Kate", "Peter", "Mark", "Sam"]);
console.log(actual.length === expected.length &&
  actual.every((value, key) => value === expected[key]));
//console.log(modifyArray(["Kate", "Peter", "Mark", "Sam"]));
// Expect true

const expected = ['Start', 10, 'mail', true, 20, 'End'];
const actual = modifyArray([false, 10, 'mail', true, 20, 30]);
console.log(actual.length === expected.length &&
  actual.every((value, key) => value === expected[key]));
//console.log(modifyArray([false, 10, 'mail', true, 20, 30]));
//Expect true

const expected = [ 'Start', 'End' ];
const actual = modifyArray([100, 200]);
console.log(actual.length === expected.length &&
  actual.every((value, key) => value === expected[key]));
//console.log(modifyArray([100, 200]));
//Expect true
