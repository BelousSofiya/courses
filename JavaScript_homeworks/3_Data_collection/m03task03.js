// Task03 - create a function with name task03
// function pass array and retun hash with min amd max values from array
// for example: 
// if function take [-1, 8, -3, 0, 7] it should return {min: -3, max: 8}

// TODO: Define your function here
function task03(arr){
    let min = 0;
    let max = 0;
    for(i=0;i<arr.length;i++){
        if(arr[i]<min){
        min = arr[i]}
        else{if(arr[i]>max){max = arr[i]}}
        }
    return {"min" : min, "max" : max};
}
console.log(task03([-1, 8, -3, -4, 0, 7]));