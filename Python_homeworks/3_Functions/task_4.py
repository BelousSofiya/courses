# Create function-generator divisor that should return all divisors of the positive number.
# If there are no divisors left function should return None.
# three = divisor(3)
# next(three) => 1
# next(three) => 3
# next(three) => None

def divisor(num):
    i = 1
    a = []
    while i * i <= num:
        if num % i == 0:
            a.append(i)
            if i != num // i:
                a.append(num // i)
        i += 1
    for i in sorted(a):
        yield i
    while True:
        yield None

#Tests

var = divisor(1)
print(next(var)) #Expect 1

two = divisor(2)
print(next(two))
print(next(two))
print(next(two))
print(next(two))
#Expect:
# 1
# 2
# None
# None

two = divisor(62832)
for _ in range(10):
  print(f'{next(two)}, ', end="")
#Expect 1, 2, 3, 4, 6, 7, 8, 11, 12, 14,
