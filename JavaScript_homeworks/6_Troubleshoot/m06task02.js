// Task02
// Your task is to create function that returns square number of an argument
// Function should check if argument is incorrect and return two different
// exceptions as instances of Error object:
// 'missing parameter' if argument is not initializated
// 'parameter is not a number' if argument is Nan

function m06task02(arg) {
    try{if(arg===undefined) throw (new Error("missing parameter"))
        //else{if(typeof arg !== 'number') throw (new Error("parameter is not a number"))}}
        else{if(isNaN(arg)) throw (new Error("parameter is not a number"))}}
    catch(err){console.log(err.message)}
};

//Tests

m06task02('a');
m06task02(1);
m06task02();
