# Write the programm that calculate total price with discount by the products.
# Use class Product(name, price, count) and class Cart. In class Cart you can add the products.
# Discount depends on count product:
# count	discount
# at least 5	5%
# at least 7	10%
# at least 10	20%
# at least 20	30%
# more than 20	50%
# Write unittest with class CartTest and test all methods with logic

import unittest

class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:
    def __init__(self, products):
        self.list_of_products = products

    def add_product(self, obj):
        self.list_of_products.append(obj)

    def count_price_with_discount(self, obj):
        lst_expr = [(obj.count < 5, 1), (5 <= obj.count < 7, 0.95),
                    (7 <= obj.count < 10, 0.9), (10 <= obj.count < 20, 0.8),
                    (obj.count == 20, 0.7), (20 < obj.count, 0.5)]
        for i in lst_expr:
            if i[0]:
                return obj.price * i[1]

    def get_total_price(self):
        tot_sum = 0
        for i in self.list_of_products:
            tot_sum += self.count_price_with_discount(i) * i.count
        return tot_sum

class CartTest(unittest.TestCase):
    def test_count_5(self):
        exmpl_prod = Product('butter', 10, 5)
        exmpl_cart = Cart([exmpl_prod])
        self.assertEqual(exmpl_cart.count_price_with_discount(exmpl_prod), 9.5)

#Tests

print(count_tests > 0)#Expect True

print(failures)#Expect 0

print(errors)#Expect 0

print(assertEqual)#Expect True

products = (Product('p1',10,4),
Product('p2',100,5),
Product('p3',200,6),
Product('p4',300,7),
Product('p5',400,9),
Product('p6',500,10),
Product('p7',1000,20))
cart = Cart(products)
print(cart.get_total_price())#Expect 24785.0