# Write  the function day_of_week(day) whose input parameter is a number or string representation of number. The function
# returns the corresponding day of the week if the input parameter is in the range of 1 to 7, namely
# · in the case when the input parameter is 5 the function should be displayed the message – "Friday"
# · in the case when the input parameter is not in the range of 1 to 7 the function should be displayed the message –
# "There is no such day of the week! Please try again."
# · in the case of incorrect data the function should be displayed the message - "You did not enter a number! Please try again."
# Note: in the function you must use the "try except" construct.
#
# Function example:
# day_of_week(2) # output:   "Tuesday"
# day_of_week(11) # output:  "There is no such day of the week! Please try again."
# day_of_week("Monday") # output:   "You did not enter a number! Please try again."

def day_of_week(day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    try:
        int(day)
    except ValueError:
        return "You did not enter a number! Please try again."
    return days[int(day) - 1] if int(day) in range(1, 8) else "There is no such day of the week! Please try again."

#Tests

print(day_of_week(5))#Expect Friday

print(day_of_week(1))#Expect Monday

print(day_of_week(0))#Expect There is no such day of the week! Please try again.

print(day_of_week(-9))#Expect There is no such day of the week! Please try again.

print(day_of_week("Sunday"))#Expect You did not enter a number! Please try again.

print(day_of_week("6"))#Expect Saturday

print(day_of_week("9"))#Expect There is no such day of the week! Please try again.