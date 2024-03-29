# You have to create a main course and a dessert at an Italian and a French restaurant, but you won't mix one cuisine with the other.
# Your task is:
# 1) define a class Product with an abstract method cook(). This class would be base class for the next classes:
# - class FettuccineAlfredo with field name ("Fettuccine Alfredo"), method cook() provides an output of the formatted
# string "Italian main course prepared: " and name of the dish;
#  - class Tiramisu, with field name ("Tiramisu"), method cook() provides an output of the formatted string
# "Italian dessert prepared:" and name of the dish;
# - class DuckALOrange, with field name ("Duck À L'Orange"), method cook() provides an output of the formatted string
# "French main course prepared: " and name of the dish;
# - class CremeBrulee,  with field name ("Crème brûlée"), method cook() provides an output of the formatted string
# "French dessert prepared: " and name of the dish.
# 2) define a class Factory with an abstract method get_dish() that takes  type_of_meal as a parameter. This class would
# be base class for the classes ItalianDishesFactory and FrenchDishesFactory. The method get_dish() according to type_of_meal
# ("main" or "dessert") invokes the dish of appropriate cousine;
# 3) define a class FactoryProducer with the method get_factory(). The method takes the parameter type_of_factory and
# invokes the appropriate dishes factory (classes ItalianDishesFactory or FrenchDishesFactory).

class Product:
    pass


class FettuccineAlfredo(Product):
    def __init__(self):
        self.name = "Fettuccine Alfredo"

    def cook(self):
        print(f"Italian main course prepared: {self.name}")


class Tiramisu(Product):
    def __init__(self):
        self.name = "Tiramisu"

    def cook(self):
        print(f"Italian dessert prepared: {self.name}")


class DuckALOrange(Product):
    def __init__(self):
        self.name = "Duck À L'Orange"

    def cook(self):
        print(f"French main course prepared: {self.name}")


class CremeBrulee(Product):
    def __init__(self):
        self.name = "Crème brûlée"

    def cook(self):
        print(f"French dessert prepared: {self.name}")

class FactoryProducer:
    def get_factory(self, name):
        if name == "italian":
            return ItalianDishesFactory()
        else:
            return FrenchDishesFactory()

class Factory:
    def get_dish(self, type_of_meal):
        pass

class ItalianDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == "main":
            return FettuccineAlfredo()
        else:
            return Tiramisu()

class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == "main":
            return DuckALOrange()
        else:
            return CremeBrulee()


#Tests

fp = FactoryProducer()
fac = fp.get_factory("italian")
main_dish = fac.get_dish("main")
main_dish.cook()
#Expect
# Italian main course prepared: Fettuccine Alfredo

dessert = fac.get_dish("dessert")
dessert.cook()
#Expect
# Italian dessert prepared: Tiramisu

fac1 = fp.get_factory("french")
main_dish = fac1.get_dish("main")
main_dish.cook()
#Expect
# French main course prepared: Duck À L'Orange

dessert = fac1.get_dish("dessert")
dessert.cook()
#Expect
# French dessert prepared: Crème brûlée