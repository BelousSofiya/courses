// Task02 - create a function with name task02
// function pass array and replace each negative number on 0 and other numbers on 1
// for example: 
// if function take array [-1, 8, -3, 0, 7] it should return [0, 1, 0, 1, 1]

// TODO: Define your function here
function task02(arr){
   for(i=0;i<arr.length;i++){
       arr[i] = (arr[i]<0)? 0:1}
   return arr;
}

console.log(task02([-1, 8, -3, 0, 7]));