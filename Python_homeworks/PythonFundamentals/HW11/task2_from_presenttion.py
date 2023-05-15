while True:
    try:
        num1, num2 = input("Write two numbers, use comma to divide them: ").split(",")
        print(f"The result of division is {int(num1) / int(num2)}")
    except ZeroDivisionError:
        print("It is forbidden to divide by zero.")
        num1, num2 = list(map(int, input("Write two numbers, use comma to divide them: ").split(",")))
    except ValueError:
        print('You wrote something wrong.')
    else:
       print("Good job!")
       break
    finally:
       print("You can try again.")
