# Given a string, check if its characters can be rearranged to form a palindrome.
# Where a palindrome is a string that reads the same left-to-right and right-to-left.
# Example
# "trueistrue" -> false;
# "abcab" -> true because "abcba" is a palindrome
# [input] string s (min 1 letters)
# [output] boolean

def isPalindrome(str):
    return sum([str.count(i)%2 for i in set(str)]) <= 1

#Tests

print(isPalindrome("abb")) #Expect True
print(isPalindrome("23332")) #Expect True
print(isPalindrome("trueitrue")) #Expect True
print(isPalindrome("trueistrue")) #Expect False
print(isPalindrome("123123")) #Expect True
print(isPalindrome("12312")) #Expect True
print(isPalindrome("qqqrrr")) #Expect False
print(isPalindrome("qqqrrrwww")) #Expect False
print(isPalindrome("A")) #Expect True


