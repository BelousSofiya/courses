//Create a Movie class, the constructor of which accepts 3 parameters: movie name name, movie genre category and start
//year of startShow.
//The class has a watchMovie() method that returns a phrase and adds a movie name name parameter to it at the end.
//For example, "I watch the movie Titanic!"
//Create an instance of the movie1 class with the title of the movie "Titanic", the genre "drama" and 1997 release.
//Create an instance of the movie2 class with the title of the movie "Troya", the genre "historical" and the 2004 release.

const Checker = require('./Checker.js');

class Movie {
    constructor(name, category, startShow) {
        this.name = name;
        this.category = category;
        this.startShow = startShow;
}
    watchMovie(){
        return "I watch the movie " + this.name + '!';
    };
}
movie1 = new Movie( "Titanic", "drama", 1997);
movie2 = new Movie("Troya", "historical", 2004);

//Tests

console.log(Checker.classHasObject(Movie, movie1));
//Expect true

console.log(Checker.classHasObject(Movie, movie2));
//Expect true

console.log(Checker.isFieldValue(movie1, "name"));
//Expect Titanic

console.log(Checker.isFieldValue(movie1, "category"));
//Expect drama

console.log(Checker.isFieldValue(movie1, "startShow"));
//Expect 1997

console.log(Checker.isFieldValue(movie2, "name"));
//Expect Troya

console.log(Checker.isFieldValue(movie2, "category"));
//Expect historical

console.log(Checker.isFieldValue(movie2, "startShow"));
//Expect 2004

console.log(movie1.watchMovie());
//Expect I watch the movie Titanic!

console.log(movie2.watchMovie());
//Expect I watch the movie Troya!