# Create function create with one string argument. This function should return anonymous function that checks if the
# argument of function is equals to the argument of outer function.
# For example:
#  tom = create("pass_for_Tom")
#  tom("pass_for_Tom") returns true
#  tom("pass_for_tom") returns false

def create(s):
    return lambda a: a == s

#Tests

# print(firstValue("secret")) #Expect True
# print(firstValue("SECRET")) #Expect False
# print(secondValue("SecreT")) #Expect True
# print(list(get_names(create))) #Expect ['']

user2 = create("___")
print(user2("__")) #Expect False