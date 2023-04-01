# 's3ooOOooDy' has exams. He wants to study hard this time. He has an array of studying hours per day for the previous
# exams. He wants to know the length of the maximum non-decreasing contiguous subarray of the studying days, to study
# as much before his current exams.
# Example:
# For a = [2,2,1,3,4,1] the answer is 3.
# [input] array.integer a
# The number of hours he studied each day.
# [output] integer
# The length of the maximum non-decreasing contiguous subarray.

def studying_hours(a):
    count_list = []
    count = 1
    for i, e in enumerate(a):
        if i > 0:
            if e < a[i-1]:
                count_list.append(count)
                count = 1
            else:
                count += 1
    return max(count_list) if count_list else len(a)

#Tests

print(studying_hours([2, 2, 1, 3, 4, 1]))
#Expect 3

print(studying_hours([2, 2, 9]))
#Expect 3

print(studying_hours([10, 100, 111, 1, 2]))
#Expect 3

print(studying_hours(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
#Expect 50

print(studying_hours(
    [1, 638, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
     1000, 1000, 1000, 1000, 1000, 1000, 1000, 1, 655, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
     1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
     1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1, 27, 533, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
     1000, 1000, 1000, 1000, 1000, 1000, 1, 835, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1,
     992]))
#Expect 42
