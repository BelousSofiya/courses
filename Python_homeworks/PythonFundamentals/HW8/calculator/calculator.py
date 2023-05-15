from decimal import Decimal


def calc(funk, num1: Decimal, num2: Decimal, action: str) -> str:
    return f"{num1} {action} {num2} = {funk(num1, num2)}"


def add(num1: Decimal, num2: Decimal) -> Decimal:
    return num1 + num2


def subtrackt(num1: Decimal, num2: Decimal) -> Decimal:
    return num1 - num2


def multiplicate(num1: Decimal, num2: Decimal) -> Decimal:
    return round(num1 * num2, 5)


def devide(num1: Decimal, num2: Decimal) -> Decimal:
    return round(num1 / num2, 5)


if __name__ == '__main__':
    assert add(5.9, 4.3) == 10.2
    assert subtrackt(11.1, 12.8) == -1.700000000000001 
    assert calc(subtrackt, 11.1, 12.8, "-") == "11.1 - 12.8 = -1.700000000000001"
    assert multiplicate(11.3, 74) == 836.2
    assert devide(2.4, 9.1) == 0.26374
