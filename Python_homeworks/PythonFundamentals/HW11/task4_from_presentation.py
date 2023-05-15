days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def check(num):
    try:
        int(num)
    except ValueError:
        raise ValueError
    else:
        if int(num) == 0:
            return 1
        else:
            return int(num)


while True:
    num = input("Write the number of the day: ")
    try:
        print(days[check(num)-1])
    except ValueError:
        print("Write only integers!")
    except IndexError:
        print("There are only 7 days in a week.")

