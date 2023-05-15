number = input('Write the integer: ')
while True:
    try:
        print("Odd" if int(number)%2 else "Even")
        break
    except ValueError:
        print("This is not an integer!")
        number = input('Write the integer: ')