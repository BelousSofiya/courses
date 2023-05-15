//Write a checkAdult(age) function whose input parameter is the age of the user age. The function checks whether the set
//age parameter is set correctly, if it is set incorrectly, the corresponding error should be generated and displayed in
//the console:
//- if the age value has not been set, you need to create the following error: "Please, enter your age",
//- If you set a negative age value, you need to create the following error: "Please, enter positive number",
//- if a non-numeric value of age was specified, you need to create the following error: "Please, enter number",
//- if the integer value of age was not specified, you need to create the following error: "Please, enter Integer number",
//- If the user is under 18, you need to create the following error: "Access denied - you are too young!".
//If there is no error, the message “Access allowed” is displayed in the console.
//In the function, implement the handling of possible exceptions, providing the output to the console of the name and
//description of the error.
//Regardless of whether the age parameter was set correctly or incorrectly, the message “Age verification complete”
//should be displayed at the end of the test.
//
//Function usage example:
//checkAdult(15);  // Error Access denied - you are too young!
//                           // Age verification complete
//checkAdult(25);  // Access allowed
//                            // Age verification complete

function checkAdult(age){
    if(arguments.length==0){
    console.log("Error Please, enter your age");
    console.log("Age verification complete");
    return}
    try{
        let a = Number(age);
        if(Number.isInteger(a)){
            if(a>=18){console.log("Access allowed")}
            else if(a>0){throw "Access denied - you are too young!"}
            else if(a<=0){throw "Please, enter positive number"}
        }
        else if(isNaN(a)){throw "Please, enter number"}
        else if(typeof a == "number"){throw "Please, enter Integer number"}
    }
    catch(error){console.log("Error "+error)}
    finally{console.log("Age verification complete")}
}

//Tests

checkAdult();
//Expect
//Error Please, enter your age
//Age verification complete

checkAdult(-22);
//Expect
//Error Please, enter positive number
//Age verification complete

checkAdult("a25");
//Expect
//Error Please, enter number
//Age verification complete

checkAdult(33.3);
//Expect
//Error Please, enter Integer number
//Age verification complete

checkAdult(16);
//Expect
//Error Access denied - you are too young!
//Age verification complete

checkAdult(20);
//Expect
//Access allowed
//Age verification complete

