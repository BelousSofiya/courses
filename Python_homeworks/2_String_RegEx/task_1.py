# As input data, you have a list of strings.
# Write a method double_string() for counting the number of strings from the list, represented in the form of the
# concatenation of two strings from this arguments  list
# For example:
# data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
# print(double_string(data))
# The result will be: 3
# data = ['aa', 'abc', 'qwerqwer']
# print(double_string(data))
# The result will be: 0

def double_string(data):
    a = [i+e for i in data for e in data if i+e in data]
    counter = len([i for i in data if i in a])
    return counter

#Tests

data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
print(double_string(data)) #Expect 3
data = ['aa', 'abc', 'qwerqwer']
print(double_string(data)) #Expect 0
data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
print(double_string(data)) #Expect 3
data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa']
print(double_string(data)) #Expect 4
