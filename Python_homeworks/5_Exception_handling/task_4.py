# Write  the function check_number_group(number) whose input parameter is a number. The function checks whether the  set
# number is more than number 10:
# if the number is more than 10 the function should be displayed the corresponding message - "Number of your group input parameter of function is valid";
# if the number is less than or equal to 10 the function should be raised the exception of your own class ToSmallNumberGroupError
# and displayed the corresponding message - "We obtain error: Number of your group can't be less than 10";
# in the case of incorrect data the function should be displayed the message - "You entered incorrect data. Please try again."
# Function example:
# check_number_group(number) (4)  #output:    "We obtain error: Number of your group can't be less than 10 "
# check_number_group(number) (59)  #output:     "Number of your group 59 is valid"
# check_number_group("25")  #output:    "Number of your group 25 is valid"
# check_number_group("abc")  #output:     "You entered incorrect data. Please try again."


class ToSmallNumberGroupError(Exception):
    def __init__(self, data):
        self.data = data

def check_number_group(number):
    try:
        if int(number) <= 10:
            raise ToSmallNumberGroupError("Number of your group can't be less than 10")
    except ValueError:
        return "You entered incorrect data. Please try again."
    except ToSmallNumberGroupError as e:
        return "We obtain error:" + str(e)
    return f"Number of your group {number} is valid"

print(check_number_group(75))#Expect Number of your group 75 is valid

print(check_number_group("96"))#Expect Number of your group 96 is valid

print(check_number_group("abc"))#Expect You entered incorrect data. Please try again.

print(check_number_group(0.8))#Expect We obtain error:Number of your group can't be less than 10

print(check_number_group(-9))#Expect We obtain error:Number of your group can't be less than 10
