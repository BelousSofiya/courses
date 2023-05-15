class Poligon:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        self.lst = [0 for i in range(self.number_of_sides)]

    def add(self):
        self.lst1 = [float(input("Write the side: ")) for i in self.lst]
        return self.lst1

class Rectangle(Poligon):

    def validate(self):
        if len(set(self.lst1)) > 2:
            raise ValueError("This is not a rectangle!")

    def get_square(self):
        self.add()
        self.validate()
        self.lst1 = list(set(self.lst1))
        if len(self.lst1) == 1:
            return self.lst1[0] ** 2
        return self.lst1[0] * self.lst1[1]

a = Rectangle(4)
sq = a.get_square()
print(sq)