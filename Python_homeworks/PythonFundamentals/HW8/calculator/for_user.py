from calculator import*
from decimal import Decimal

num1 = Decimal(input("Write first number: "))
num2 = Decimal(input("Write second number: "))
action = input("What do you want to do? Write +, -, *, : ")
    
match action:
    case "+":
        print(calc(add, num1, num2, action))
    case "-":
        print(calc(subtrackt, num1, num2, action))
    case "*":
        print(calc(multiplicate, num1, num2, action))
    case ":":
        print(calc(devide, num1, num2, action))
    
