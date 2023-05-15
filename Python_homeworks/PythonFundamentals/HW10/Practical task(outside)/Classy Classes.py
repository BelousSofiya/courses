class Person:
    def __init__(self,name,age):
        if type(name) == str:
            self.name = name
        if type(age) in [float, int]:
            self.age = age

        self.info = f"{name}s age is {age}"
