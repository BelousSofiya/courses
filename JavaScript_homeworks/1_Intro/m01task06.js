// Task06 - Write a code that returns number - result of sum 3 numbers:
// -- first should be extracted from String, second - should be Boolean.
// For example, "10" and true - as a result you get 11 
// or "2long" and true give you 3.

function task06(string, boolean) {
    let a=prompt("first digit:")
    let b=Boolean(prompt("second digit:"))
    let c=prompt("third digit:")
    return Number(parseInt(a.match(/\d+/)))+b+Number(c)// TODO: Write your code here
}
d=task06()
alert(d)