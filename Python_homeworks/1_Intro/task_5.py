# Convert a certain expression like 2+3 to expression in a postfix notation.
# The given expression can have one of the following tokens:
# a number;
# a parenthesis;
# arithmetic operator:
# subtraction (-);
# addition (+);
# multiplication (*);
# devision (/);
# modulo operation (%).
# Example:
# For expression = ["2","+","3"] the output should be ["2","3","+"].
# [execution time limit] 4 seconds (py)
# [input] array.string expression
# An array of tokes of a valid expression in the standard notation.
# [output] array.string
# Tokens of the expression in the postfix notation.

def toPostFixExpression(e):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = []
    postfixList = []
    tokenList = e

    for token in tokenList:
        if token.isdigit():
            postfixList.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while opStack and (prec[opStack[0]] >= prec[token]) and opStack[-1] != '(':
                  postfixList.append(opStack.pop())
            opStack.append(token)

    while opStack:
        postfixList.append(opStack.pop())
    return postfixList

#Tests

print(toPostFixExpression(["2",
                           "+",
                           "3"]))
#Expect ['2', '3', '+']

print(toPostFixExpression(["20",
                           "+",
                           "3",
                           "*",
                           "(",
                           "5",
                           "*",
                           "4",
                           ")"]))
#Expect ['20', '3', '5', '4', '*', '*', '+']

print(toPostFixExpression(["(",
                           "(",
                           "(",
                           "1",
                           "+",
                           "2",
                           ")",
                           "*",
                           "3",
                           ")",
                           "+",
                           "6",
                           ")",
                           "/",
                           "(",
                           "2",
                           "+",
                           "3",
                           ")"]))
#Expext ['1', '2', '+', '3', '*', '6', '+', '2', '3', '+', '/']