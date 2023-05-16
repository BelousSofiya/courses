# Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords.
# Each instance should have a name and a lastname attributes plus one more attribute for each of the keywords, if any.
# Examples:
# john = Employee("John Doe")
# mary = Employee("Mary Major", salary=120000)
# richard = Employee("Richard Roe", salary=110000, height=178)
# giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
# mary.lastname ➞ "Major"
# richard.height ➞ 178
# giancarlo.nationality ➞ "Italian"
# john.name ➞ "John"

class Employee:
    def __init__(self, full_name, **kwargs):
        self.name = full_name.split()[0]
        self.lastname = full_name.split()[1]
        for key in kwargs:
            setattr(self, key, kwargs[key])

#Tests

john = Employee('John Doe')
print(john.lastname)#Expect Doe

mary = Employee('Mary Major', salary=120000)
print(mary.salary)#Expect 120000

richard = Employee('Richard Roe', salary=110000, height=178)
print(richard.salary)
print(richard.height)
#Expect
# 110000
# 178

giancarlo = Employee('Giancarlo Rossi', salary=115000, height=182, nationality='Italian')
print(giancarlo.name)
print(giancarlo.nationality)
#Expect
# Giancarlo
# Italian

peng = Employee('Peng Zhu', salary=500000, height=185, nationality='Chinese', subordinates=[i.lastname for i in (john, mary, richard, giancarlo)])
print(peng.subordinates)
#Expect ['Doe', 'Major', 'Roe', 'Rossi']
