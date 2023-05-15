//The function filterByN receives an array of integers, a number and a parameter (greater, less). Print a new array,
//where all elements will be greater/less than this number
//By default, the number is 0, the parameter is greater.
//Example:
//filterNums([-1, 2, 4, 0, 55, -12, 3], 11, 'greater');  //[ 55]
//filterNums([-2, 2, 3, 0, 43, -13, 6], 6, 'less'); // [-2, 2, 3, 0, -13]
//filterNums([-2, 2, 3, 0, 43, -13, 6], -33, 'less'); //  []
//filterNums([-2, 2, 3, 0, 43, -13, 6]); // [2, 3, 43, 6]
//filterNums([-2, 2, 3, 0, 43, -13, 6], 23);  // [43]

const filterNums = (arr, number=0, action='greater') => {
    let a;
    if(action == 'greater'){
    a = arr.filter((item) => {
    return item > number
  });
}
    else{
    a = arr.filter((item) => {
    return item < number
  })
}
    return a;
};

//Tests

console.log(filterNums([-3, 3, 4, 0, 44, -11, 5], 11, 'greater'));//Expect [ 44 ]

console.log(filterNums([-3, 3, 4, 0, 44, -11, 5], 5, 'less'));//Expect [ -3, 3, 4, 0, -11 ]

console.log(filterNums([-3, 3, 4, 0, 44, -11, 5], -30, 'less'));//Expect []

console.log(filterNums([-3, 3, 4, 0, 44, -11, 5]));//Expect [ 3, 4, 44, 5 ]

console.log(filterNums([-3, 3, 4, 0, 44, -11, 5], 9));//Expect [ 44 ]