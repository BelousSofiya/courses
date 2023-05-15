//Find the maximum interval between two consecutive numbers. Numbers are entered as arguments
//Example:
//maxInterv(3, 5, 2, 7); //5
//maxInterv(3, 5, 2, 7, 11, 0, -2); //11
//maxInterv(3, 5); //2
//maxInterv(3); //0

const maxInterv = (...arguments) => {
let total = [];
  for (let i = 0; i < arguments.length-1; i++){
      arg = arguments[i+1]-arguments[i]
    total = total.concat([Math.abs(arg)]);
  }
  if(arguments.length == 1){return 0}
  else{
  return Math.max(...total);
  };
};

//Tests

console.log(maxInterv(3, 5, 2, 7))//Expect 5

console.log(maxInterv(3, 5, 2, 7, 11, 0, -2))//Expect 11

console.log(maxInterv(3, 5))//Expect 2

console.log(maxInterv(3));//Expect 0

console.log(maxInterv(3, 5, 2, 8));//Expect 6

console.log(maxInterv(3, 5, 2, 37, 11, 0, -2))//Expect 35

console.log(maxInterv(8));//Expect 0