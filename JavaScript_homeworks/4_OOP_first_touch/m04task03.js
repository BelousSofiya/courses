// Task03 - Update your constructor Cat from task 2
// Constructor should add to objects method action()
// After calling method action return string with next format:
// color + " cat " + name + " run!"

// For example if cat created with parameters "white" and "Lucky"
// it action() should be "white cat Lucky run!"

// P.S
// Remember about this

function task03(color, name) {
    function Cat(color, name){
        this.name = name;
        this.color = color;
        this.action = (act) => this.color + " cat " + this.name + " " + act;
    }
    return new Cat(color, name); // don't change this code
}
let lucky = task03("white-red", "Lucky")
console.log(lucky.name)
console.log(lucky.color)
console.log(lucky.action("sleeps"))

