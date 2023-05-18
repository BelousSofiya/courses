# Create a Pizza class with the attributes order_number and ingredients (which is given as a list). Only the ingredients
# will be given as input.
# You should also make it so that its possible to choose a ready made pizza flavour rather than typing out the
# ingredients manually! As well as creating this Pizza class, hard-code the following pizza flavours.
# Examples:
# p1 = Pizza(["bacon", "parmesan", "ham"])   # order 1
# p2 = Pizza.garden_feast()                  # order 2
# p1.ingredients ➞ ["bacon", "parmesan", "ham"]
# p2.ingredients ➞ ["spinach", "olives", "mushroom"]
# p1.order_number ➞ 1
# p2.order_number ➞ 2

class Pizza:
    order_number = 0
    def __init__(self, *ingredients):
        self.order_number = Pizza.order_number + 1
        self.ingredients = ingredients[0]
        Pizza.order_number += 1

    @staticmethod
    def hawaiian():
        return Pizza(["ham", "pineapple"])

    @staticmethod
    def meat_festival():
        return Pizza(["beef", "meatball", "bacon"])

    @staticmethod
    def garden_feast():
        return Pizza(["spinach", "olives", "mushroom"])

#Tests

p1 = Pizza(['bacon', 'parmesan', 'ham'])
print(p1.ingredients)
#Expect ['bacon', 'parmesan', 'ham']

p2 = Pizza.garden_feast()
print(p2.ingredients)
#Expect ['spinach', 'olives', 'mushroom']

p3 = Pizza.hawaiian()
print(p3.ingredients)
#Expect ['ham', 'pineapple']

p4 = Pizza.meat_festival()
print(p4.ingredients)
#Expect ['beef', 'meatball', 'bacon']

p5 = Pizza(["pepperoni", "bacon"])
print(p5.ingredients)
#Expect ['pepperoni', 'bacon']

my_pizza = Pizza(['cheese', 'caviar', 'oyster', 'uranium'])
print(my_pizza.ingredients)
#Expect ['cheese', 'caviar', 'oyster', 'uranium']

print(p1.order_number)
print(p2.order_number)
print(p3.order_number)
print(p4.order_number)
print(p5.order_number)
print(my_pizza.order_number)
#Expect
# 1
# 2
# 3
# 4
# 5
# 6