from random import randint
lenth = int(input("Tell us lenth of the list"))
limit_number = int(input("Indicate the upper limit of values"))

#first variant

lst = []
for i in range(lenth):
    lst.append(float(randint(0, limit_number)))
print(lst)


#other variant

print([float(randint(0, limit_number)) for i in range(lenth)])
