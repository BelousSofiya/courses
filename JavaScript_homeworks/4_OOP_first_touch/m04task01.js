// Task01 - Create a simple object cat and return it from function.
//
// Object should have next attributes:
// color with value "white"
// age with value 3
// name - Lucky

function task01() {
    function Cat(name, color, age){
        this.name = name;
        this.color = color;
        this.age = age;
    }
    return new Cat('Lucky', 'white', 3);
}
let lucky = task01()
console.log(lucky.name)
console.log(lucky.color)
console.log(lucky.age)
