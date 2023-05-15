fibonacci_range = int(input("Indicate the lenth of Fibonacci line"))

lst = []
for i in range(fibonacci_range):
    if i == 0 or i == 1:
        lst.append(i)
    else:
        lst.append(lst[i-1]+lst[i-2])
print(lst)

