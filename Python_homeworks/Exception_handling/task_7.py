# Write the function sum_slice_array(arr, first, second), which accepts the array (list) arr and two numbers (first and
# second) - the ordinal numbers of the elements of the array that must be added. For example, if 3 and 5 were entered,
# the 3rd and 5th elements must be added.
# The function should generate exceptions MyExceptions:
# if non-numbers or numbers less than 1 were entered;
# if non-numbers obtained from array;
# if when one of the numbers or both is larger than the array length.
# For example:
# Test	                                                           Result
# print(sum_slice_array([1, 2, 3], 1, 2))                            3.0
# try:
#     print(sum_slice_array([1, "string", 3], 1, 2))
# except MyExceptions:
#     print("MyExceptions")                                          MyExceptions
# try:
#     print(sum_slice_array([14, 5, 3], -1, 2))
# except MyExceptions:
#     print("MyExceptions")                                          MyExceptions

class MyExceptions(Exception):
    pass

def sum_slice_array(arr, first, second):
    if any([first > len(arr) or second > len(arr),
              type(first) != int or type(second) != int,
              first < 1 or second < 1,
              type(arr[first-1]) != int or type(arr[second-1]) != int,
              ]):
        raise MyExceptions
    return float(arr[first - 1] + arr[second - 1])

#Tests

print(sum_slice_array([1, 2, 3], 1, 2))
# Expect 3.0

try:
    print(sum_slice_array([1, "string", 3], 1, 2))
except MyExceptions:
    print("MyExceptions")
# Expect MyExceptions

try:
    print(sum_slice_array([14, 5, 3], -1, 2))
except MyExceptions:
    print("MyExceptions")
# Expect MyExceptions

try:
    print(sum_slice_array([14, 5, 3], 1, -2))
except MyExceptions:
    print("MyExceptions")
# Expect MyExceptions

try:
    print(sum_slice_array([7, 9, 3, 6, 7], 5, 2))
except MyExceptions:
    print("MyExceptions")
# Expect 16.0

try:
    print(sum_slice_array([7, 9, 3, 6, 7], 3, 3))
except MyExceptions:
    print("MyExceptions")
# Expect 6.0

try:
    print(sum_slice_array([7, 9, 3, 6, 7], 0, 0))
except MyExceptions:
    print("MyExceptions")
# Expect MyExceptions