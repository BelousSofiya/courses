num = input()
lst = []
total = 1
for i in range(len(num)):
    lst.append(int(num[i]))
    total *= int(num[i])
print(total, int(num[::-1]), "".join(sorted(num)), sep = "\n")

