# Create function create_account(user_name: string, password: string, secret_words: list). This function should return
# inner function check.
# The function check compares the values of its arguments with password and secret_words: the password must match
# completely, secret_words may be misspelled (just one element).
# Password should contain at least 6 symbols including one uppercase letter, one lowercase letter,  special character
# and one number.
# Otherwise function create_account raises ValueError.
# For example:
# tom = create_account("Tom", "Qwerty1", ["1", "word"]) raises Value error
# If tom = create_account("Tom", "Qwerty1_", ["1", "word"])
# then
# tom("Qwerty1_",  ["1", "word"]) return True
# tom("Qwerty1_",  ["word"]) return False due to different length of   ["1", "word"] and  ["word"]
# tom("Qwerty1_",  ["word", "12"]) return True
# tom("Qwerty1!",  ["word", "1"]) return False because "Qwerty1!" not equals to "Qwerty1_"

import re
def create_account(user_name, password, secret_words):
    for i in ['([A-Z])', '([a-z])', '([0-9])', '([\W_])', '(([\w\W]{6,}))']:
        if not re.findall(fr'{i}', password):
            raise ValueError
    def check(b, c):
        if len(c) == len(secret_words):
            cop = secret_words[:]
            for i in c:
                if i in cop:
                    cop.remove(i)
            return b == password if len(cop) <= 1 else False
        else:
            return False
    return check
#Code was given by default:
tom = create_account("Tom", "Qwerty1_", ["1", "word"])
check1 = tom("Qwerty1_",  ["1", "word"])
check2 = tom("Qwerty1_",  ["word"])
check3 = tom("Qwerty1_",  ["word", "2"])
check4 = tom("Qwerty1!",  ["word", "12"])

#Unfortunetally, functions in tests and some input data were hidden:

val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_1_true))
#Expect True

val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_2_true))
#Expect True

val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_3_true))
#Expect True

print('check' in list(get_names(create_account)))
#Expect True

val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_4_true))
#Expect True

val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_5_true))
#Expect True

val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_6_true))
#Expect True

val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_7_false))
#Expect False

val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_8_false))
#Expect False

val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_9_false))
#Expect False

try:
    val1 = create_account("123", "qQ1345", initial_arr)
except ValueError:
    print("Raises ValueError")
#Expect Raises ValueError

print(check1,check2,check3,check4)
#Expect True False True False

user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
print(user2("yu6r*Tt5",["abc3", "word1", "list"]))
#Expect True

user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
print(user2("yu6r*Tt5",["abc3", "word1", "zzzzzz"]))
#Expect True

user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
print(user2("yu6r*Tt5",["abc3", "abc3", "abc3"]))
#Expect False

user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
print(user2("yu6r*Tt5",["word1", "zzzz", "z"]))
#Expect False

user3 = create_account("User", "MmKk*9kj", ["1", "2", "1"])
print(user3("MmKk*9kj", initial_arr))
#Expect True

try:
  simple_user = create_account("A", "Aa!1", ["word"])
except ValueError:
  print("Raises ValueError")
#Expect Raises ValueError

simple_user = create_account("A", "Aa!190", ["word"])
print(simple_user("Aa!190", ["word"]))
#Expect True