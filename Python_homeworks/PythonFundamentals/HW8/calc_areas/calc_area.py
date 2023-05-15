from math import pi


def calc_area(funk, figure: str) -> str:
    return f"The area of your {figure} is {funk}"
    
def get_rectangle(width: float, lenth: float) -> float:
    return round(width * lenth, 5)


def get_circle(radius: float) -> float:
    return round(pi * radius ** 2, 5)


def get_triangle(height: float, width: float) -> float:
    return round(0.5 * height * width, 5)
