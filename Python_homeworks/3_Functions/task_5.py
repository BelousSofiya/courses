# Create decorator logger. The decorator should print to the console information about function's name and all its
# arguments separated with ',' for the function decorated with logger.
# Create function concat with any numbers of any arguments which concatenates arguments and apply logger decorator for
# this function.
# For example
# print(concat(2, 3)) display
# Executing of function concat with arguments 2, 3...
# 23
# print(concat('hello', 2)) display
# Executing of function concat with arguments hello, 2...
# hello2
# print(concat (first = 'one', second = 'two')) display
# Executing of function concat with arguments one, two...
# onetwo

def logger(funk):
    def wrapper(*args, **kwargs):
        b = args + tuple(kwargs.values())
        s = ''
        for i in b:
            s += str(i) + ", "
        s = s.rstrip(", ")
        a = funk(*args, **kwargs)
        print(f"Executing of function {funk.__name__} with arguments {s}...")
        return funk(*args, **kwargs) if a else ""
    return wrapper

@logger
def concat(*args, **kwargs):
    s = ''
    for i in args:
        s += str(i)
    for i in kwargs:
        s += str(kwargs[i])
    return s

#Code was given by default:
@logger
def sum(a, b):
    return a + b

@logger
def print_arg(arg):
    print(arg)

#Tests

print(concat(1))
# Executing of function concat with arguments 1...
# 1

print(concat('first string', second=2, third='second string'))
# Executing of function concat with arguments first string, 2, second string...
# first string2second string

print(concat('first string', {'first kwarg': 0, 'second kwarg': 'second kwarg'}))
#Executing of function concat with arguments first string, {'first kwarg': 0, 'second kwarg': 'second kwarg'}...
#first string {'first kwarg': 0, 'second kwarg': 'second kwarg'}

print(sum(2, 3))
#Executing of function sum with arguments 2, 3...
#5

dict_args = {'first kwarg': 0, 'second kwarg': 'second kwarg'}
concat(**dict_args)

#Executing of function concat with arguments 0, second kwarg...

print_arg(2)
# 2
#Executing of function print_arg with arguments 2...