def check(age):
    try:
        if int(age) < 0:
            raise ValueError
    except ValueError:
        return "It's impossible."
    else:
        return "Odd" if int(age)%2 else "Even"


while True:
    try:
        age = int(input("Write your age: "))
    except ValueError:
        print("Write only integers!")
    else:
        print(check(age))
