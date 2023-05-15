//Implement the Student class, the constructor of which accepts 2 parameters fullName - the name and surname of the
//student, direction - the direction in which he studies.
//Create a showFullName() method that returns the student's first and last name.
//Create a nameIncludes(data) method that, using the showFullName() method, checks for the text data argument in the
//student’s name and returns true if a match is found or false if not found.
//Create a static studentBuilder() method that returns a new instance of the class named ‘Ihor Kohut’ and the direction ‘qc’.
//Create a getter and setter direction() to read and specify the direction field.
//Create an instance of class stud1 named 'Ivan Petrenko' and direction 'web'.
//Create an instance of class stud2 named 'Sergiy Koval' and direction 'python'.
//Create an instance of the stud3 class named ‘Ihor Kohut’ and the direction ‘qc’ using the static studentBuilder() method.
//Usage example:
//const stud1 = new Student('Ivan Petrenko', 'web');
//stud1.nameIncludes('Ivan');   // true
//stud1.nameIncludes('Denysenko'); // false

class Student {

    constructor(fullName, direction) {
      this._fullName = fullName;
      this._direction = direction;
    }
    showFullName(){return this._fullName};
    nameIncludes(data){
        if(this.showFullName().includes(data)){return true}
        else{return false};
    };
    static studentBuilder(){return new Student('Ihor Kohut','qc')};
    get direction(){return this._direction};
    set direction(direction){this._direction = direction};
    }

stud1 = new Student('Ivan Petrenko', 'web');
stud2 = new Student('Sergiy Koval', 'python');
stud3 = Student.studentBuilder();

//Tests

console.log(stud1.nameIncludes('Ivan'));//Expect true

console.log(stud1.nameIncludes('Petrenko'));//Expect true

console.log(stud1.nameIncludes('Ihor'));//Expect false

console.log(stud2.nameIncludes('Sergiy'));//Expect true

console.log(stud2.nameIncludes('Koval'));//Expect true

console.log(stud2.nameIncludes('Ivan'));//Expect false

console.log(stud3.nameIncludes('Ihor'));//Expect true

console.log(stud3.nameIncludes('Kohut'));//Expect true

console.log(stud3.nameIncludes('Petrenko'));//Expect false

console.log(stud1.showFullName());//Expect Ivan Petrenko

console.log(stud2.showFullName());//Expect Sergiy Koval

console.log(stud3.showFullName());//Expect Ihor Kohut

console.log(Student.studentBuilder());//Expect Student { _fullName: 'Ihor Kohut', _direction: 'qc' }

console.log(stud1.direction);//Expect web

console.log(stud2.direction);//Expect python

console.log(stud3.direction);//Expect qc

stud2.direction = "Java";
console.log(stud2.direction);//Expect Java