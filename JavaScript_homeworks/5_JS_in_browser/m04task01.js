// Task01 - Create a simple function that will be used as event handler. 
// function should cancel event bubbling

function task01() {
    b.addEventListener("click", action, false)}
function action(e){
    e = e||window.event;
    console.log("!!!");
    alert("!!!")}

task01()