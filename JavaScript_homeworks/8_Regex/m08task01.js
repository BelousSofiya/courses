// Task01 - create regular expression which tests for corectness phone numbers.
// Phone number should have 10 digits optionally divided to 3-digit groups by periods ("."), dashes ("-"),
// brackets ("()"), or space symbols (" "). Brackets should be used only at the beginning
// Examples of correct phone numbers:
// (123) 456 7899
// (123).456.7899
// (123)-456-7899
// 123-456-7899
// 123 456 7899
// 1234567899

function task01(testNumber) {
    // TODO: Define your regular expression here, test "testNumber" string and return function result as boolean
    let re = /^\(\d{3}\)(\.|-|_| )?\d{3}(\.|-|_| )?\d{4}$/;
    let re1 = /^\d{3}(\.|-|_| )?\d{3}(\.|-|_| )?\d{4}$/;
    return re.test(testNumber)||re1.test(testNumber);
}

//returns true
console.log(task01('(123) 456 7899'));
console.log(task01('(123).456.7899'));
console.log(task01('(123)-456-7899'));
console.log(task01('123-456-7899'));
console.log(task01('123 456 7899'));
console.log(task01('1234567899'));

//returns false
console.log(task01('(123 456 7899'));
console.log(task01('(123)   456-7899'));
console.log(task01('123))-456-7899'));
console.log(task01('123...456 7899'));
console.log(task01('123-456-78'));