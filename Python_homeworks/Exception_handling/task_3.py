# Write the function valid_email(...) to check if the input string is a valid email address or not.
# An email is a string (a subset of ASCII characters) separated into two parts by @ symbol,
# a “user_info” and a domain_info, that is personal_info@domain_info:
# in case of correct email the function should be displayed the corresponding message – "Email is valid"
# in case of incorrect email the function should be displayed the corresponding message – "Email is not valid"
# Note: in the function you must use the "try except" construct.
# For example:
# Test	                                  Result
# print(valid_email("trafik@ukr.tel.com"))  Email is valid
# print(valid_email("trafik@ukr_tel.com"))  Email is not valid
# print(valid_email("ownsite@our.c0m"))     Email is not valid
# print(valid_email("tra@fik@ukr.com"))     Email is not valid

import re
def valid_email(email):
    inf = email.split("@")
    try:
        user = re.findall(r"([a-z]+)", inf[0])[0]
        domain = re.findall(r"([a-z.]+)", inf[1])[0]
    except (ValueError, IndexError):
        return "Email is not valid"
    true = len(inf) == 2 and inf[0] == user and inf[1] == domain
    return "Email is valid" if true else "Email is not valid"

#Tests

print(valid_email("trafik@ukr.tel.com"))#Expect Email is valid

print(valid_email("trafik@ukr_tel.com"))#Expect Email is not valid

print(valid_email("ownsite@our.c0m"))#Expect Email is not valid

print(valid_email("probaggdf@gmail.hhh.com"))#Expect Email is valid

print(valid_email("tra@fik@ukr.com"))#Expect Email is not valid

print(valid_email("example@source_arth.com"))#Expect Email is not valid

print(valid_email("exam@ple@sourcepath.com"))#Expect Email is not valid

print(valid_email("examplesource_arth.com"))#Expect Email is not valid

print(valid_email("example@source.ua"))#Expect Email is valid