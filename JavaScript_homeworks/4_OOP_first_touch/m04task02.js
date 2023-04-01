// Task02 - Create constructor Cat reproducing it objects
// constructor should set 2 parameters - name and color
// and and use it as a object attributes 

function task02(color, name) {

    function Cat(name, color){
        this.name = name;
        this.color = color;
    }
    return new Cat(color, name); // don't change this code
}

// TODO: Define your constructor here
let lucky = task02("red", "Murzick")
console.log(lucky.name)
console.log(lucky.color)
