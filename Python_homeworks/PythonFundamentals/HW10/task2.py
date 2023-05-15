class Human:
    @staticmethod
    def validate(x):
        return type(x) == str

    def __init__(self, name, species="Homosapiens"):
        if self.validate(name) and self.validate(species):
            self.name = name
            self.species = species
        else:
            raise TypeError("Only strings!")

    def greeting(self):
        return f"Hello, {self.name}"

    @staticmethod
    def print_something():
        return "Something fun"

a = Human("John")
print(a.name, a.species)
print(a.greeting())
print(Human.print_something())