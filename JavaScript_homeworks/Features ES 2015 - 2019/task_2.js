//The user enters as arguments the number of seconds, minutes, hours, days, weeks, months, years.
//Output how many seconds are in all this.
//All parameters are optional. Consider 30 days in a month
//Example:
//howMuchSec(12, 3); //192
//howMuchSec(1, 33, 22); //81181
//howMuchSec(); //0

const howMuchSec = (sec=0, min=0, hour=0, day=0, week=0, month=0, year=0) => {
    return sec + min * 60 + hour * 60 * 60 + day * 24 * 60 * 60 + week * 7 * 24 * 60 * 60 + month * 30 * 24 * 60 * 60 + year * 365 * 24 * 60 * 60;

};

//Tests

console.log(howMuchSec(12, 3));//Ex[ect 192

console.log(howMuchSec(1, 33, 22));//Expect 81181

console.log(howMuchSec());//Expect 0

console.log(howMuchSec(12, 3, 3, 3));//Expect 270192

console.log(howMuchSec(33, 33, 11));//Expect 41613
