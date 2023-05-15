def solution(number):
    if number > 0:
        return sum([i for i in range(number) if (not i%3) or (not i%5)])
    else:
        return 0

