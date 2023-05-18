# We have a function calc(a, b, op) as shown on screenshot.
# Write your code insode run_calc with calling of function calc. Script must work with any arguments. Catch ValueError and
# print it, catch TypeError and print "TypeError", Catch error of division by zero and print "Division by zero".
# After call calc print "End of calculation" in all cases.
# def calc(a, b, op):
#     if op == 0:
#         return a + b
#     if op == 1:
#         return a - b
#     if op == 2:
#         return a * b
#     if op == 3:
#         return a / b
#     raise ValueError("Incorrect operation is obtained")

def run_calc(a, b, op):
    try:
        res = calc(a, b, op)
    except ZeroDivisionError:
        print(f"Division by zero")
    except ValueError as e:
        print(f"{e}")
    except TypeError:
        print("TypeError")
    else:
        print(res)
    finally:
        print("End of calculation")

#Tests

run_calc(1, 2, 0)
#Expect
# 3
# End of calculation

run_calc(-19, 2, 1)
#Expect
# -21
# End of calculation

run_calc(-19, "String", 3)
#Expect
# TypeError
# End of calculation

run_calc(42, 0, 3)
#Expect
# Division by zero
# End of calculation

run_calc(15, 3, 3)
#Expect
# 5.0
# End of calculation

run_calc(8, 2, 4)
#Expect
# Incorrect operation is obtained
# End of calculation

run_calc("String", 2, 3)
#Expect
# TypeError
# End of calculation

run_calc(0, 0, 5)
#Expect
# Incorrect operation is obtained
# End of calculation