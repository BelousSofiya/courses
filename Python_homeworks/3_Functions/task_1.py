# Create function with name outer(name). This function should return inner function with name inner.
# This inner function prints message Hello, <name>!
# For example
# tom = outer("tom")
# tom() -> Hello, tom!

def outer(name):
    def inner():
        print(f"Hello, {name}!")
    return inner

#Tests

if ('outer' in locals()):
 print('function "outer" is present')
else:
 print('function "outer" is absent')
#Expect function "outer" is present

outer("Tom")() #Expect Hello, Tom!

alice = outer("Alice")
alice() #Expect Hello, Alice!
