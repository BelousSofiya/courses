from math import factorial
num = abs(int(input()))
print(factorial(num))

#other variant

num = int(input())
factorial = 1
if num < 0:
    print("Impossible operation")
else:
    while num > 0:
        factorial *= num
        num -= 1
print(factorial)
