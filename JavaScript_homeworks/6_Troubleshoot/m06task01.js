// Task01 
// Your task is to check if arument is undefined and if it is true, 
// throw an exception of type Error with message 'missing parameter'

function m06task01(arg) {
    try{if(arg===undefined) throw (new Error("missing parameter"))}
    catch(err) {console.log(err.message)};
};

//Tests

m06task01('a');
m06task01(1);
m06task01();
