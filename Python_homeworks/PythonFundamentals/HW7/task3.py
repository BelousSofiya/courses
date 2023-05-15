def calculate_char(word):
    calc = {}
    for i in word:
        calc.setdefault(i, word.count(i))
    return calc
dic = calculate_char("hello pytyhonnn")
print(dic)

# other variant

def calculate_char(word):
    return {i:word.count(i) for i in word}
    
dic = calculate_char("hi kitty")
print(dic)
