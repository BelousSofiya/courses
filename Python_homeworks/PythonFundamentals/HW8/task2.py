password = input("Write your password ")

while True:
    try:
        assert 6 <= len(password) <= 16
        assert any([i for i in password if i in "#$@"])
        assert any([i.isdigit() for i in password])
        assert any([i for i in password if i.isalpha() and i == i.upper()])
        assert any([i for i in password if i.isalpha() and i == i.lower()])
        print("Greetings! Wonderful password!")
        break
    except AssertionError:
        print("Too weak password. Try again!")
        password = input("Write your password")


#other variant

import re

password = input("Other variant. Write your password ")

lst = [r'.{6,16}', r'[A-Z]', r'[a-z]', r'[0-9]', r'\W']
lst2 = [(re.findall(i, password)) for i in lst]
print("Secure password!" if all(lst2) else "Insecure password")



