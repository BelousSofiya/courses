//Write a function combineArray(arr1, arr2), which takes 2 arrays, and returns a new array consisting only of numeric
//elements of arrays arr1 and arr2.
//Function example:
//combineArray([12, "User01", 22, true, -8], ["Index", 6, null, 15]));  // [12, 22, -8, 6, 15]

function combineArray(arr1, arr2) {
    a = arr1.filter(function(item) {
        if(typeof item == "number"){
            return item}
    });
    b = arr2.filter(function(item) {
        if(typeof item == "number"){
            return item}
    });
    return a.concat(b);
}

//Tests

const expected = [ 12, 22, -8, 6, 15 ];
const actual = combineArray([12, "User01", 22, true, -8], ["Index", 6, null, 15]);
console.log(actual.length === expected.length &&
  actual.every((value, key) => value === expected[key]));
//console.log(combineArray([12, "User01", 22, true, -8], ["Index", 6, null, 15]));
//Expect true

const expected = [ 33, 44 ];
const actual = combineArray(["User01", "User02", "User03", "User04"], ["Data1", 33, "Data2", 44]);
console.log(actual.length === expected.length &&
  actual.every((value, key) => value === expected[key]));
//console.log(combineArray(["User01", "User02", "User03", "User04"], ["Data1", 33, "Data2", 44]));
//Expect true

const expected = [ 10, 20, 30 ];
const actual = combineArray([10, 20, 30], ["Data1", "Data2", "Data3", "Data4", "Data5"]);
console.log(actual.length === expected.length &&
  actual.every((value, key) => value === expected[key]));
//console.log(combineArray([10, 20, 30], ["Data1", "Data2", "Data3", "Data4", "Data5"]));
//Expect true

const expected = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ];
const actual = combineArray([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]);
console.log(actual.length === expected.length &&
  actual.every((value, key) => value === expected[key]));
//console.log(combineArray([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]));
//Expect true

const expected = [];
const actual = combineArray(['1', '2', '3', '4' ], ['first', 'second', 'third']);
console.log(actual.length === expected.length &&
  actual.every((value, key) => value === expected[key]));
//console.log(combineArray(['1', '2', '3', '4' ], ['first', 'second', 'third']));
//Expect true

