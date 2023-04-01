# For the given integer n, consider an increasing sequence consisting of all positive integers that are either powers of n,
# or sums of distinct powers of n.
# Your task is to find the kth (1-based) number in this sequence.
# Example
# For n = 3 and k = 4, the output should be
# kthTerm(n, k) = 9.
# For n = 3, the sequence described above begins as follows: 1, 3, 4, 9, 10, 12, 13...
# [3**0] => [1]
# [1, 3**1, 3**1 +1] => [1, 3, 4]
# [1, 3, 4, 3**2, 3**2 +1, 3**2 +3, 3**2 +4] => [1, 3, 4, 9, 10, 12, 13]
# ...
# The 4th number in this sequence is 9, which is the answer.
# Input/Output
# [input] integer n
# The number to build the sequence by.
# Constraints:
# 2 ≤ n ≤ 30.
# [input] integer k
# The 1-based index of the number in the sequence.
# Constraints:
# 1 ≤ k ≤ 100.
# [output] integer
# The kth element of the sequence.

def kthTerm(n, k):
    result = []
    for i in range(n+1):
        result.append(n**i)
        if len(result) >= k:
            return result[k - 1]
        else:
            result.extend([n ** i + e for e in result[:-1]])
    return result[k - 1]

#Tests

print(kthTerm(3, 4)) #Expect 9
print(kthTerm(3, 7)) #Expect 13
print(kthTerm(3, 3)) #Expect 4
print(kthTerm(2, 7)) #Expect 7
print(kthTerm(4, 3)) #Expect 5
print(kthTerm(30, 100)) #Expect 753300900
print(kthTerm(2, 1)) #Expect 1
print(kthTerm(15, 50)) #Expect 810015
print(kthTerm(21, 63)) #Expect 4288306
print(kthTerm(10, 99)) #Expect 1100011