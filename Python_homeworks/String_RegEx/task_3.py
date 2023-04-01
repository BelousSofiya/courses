# The string defining the points of the quadrilateral has the next form: "#LB1:1#RB4:1#LT1:3#RT4:3"
#  LB - Left Bottom point
#  LT - Left Top point
#  RT - Right Top point
#  RB - Right Bottom point
# numbers after letters are the coordinates of a point.
# Write a function figure_perimetr() that calculates the perimeter of a quadrilateral
# The formula for calculating the distance between points:
# square root((x2 - x1)**2 + (y2 - y1)**2)
# For example:
# test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
# print(figure_perimetr(test1))
# Output: 10.0
# test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
# print(figure_perimetr(test2))
#Output: 18.73454147995595

import re

def figure_perimetr(data):
    a = re.findall(r'([A-Z][A-Z])', data)
    x = lambda i: int(*re.findall(fr'[\w\#:]*{i}(\d)[\w\#:]*', data))
    y = lambda i: int(*re.findall(fr'[\w\#:]*{i}\d:(\d)[\w\#:]*', data))
    coords = {i:(x(i), y(i)) for i in a}
    lenth = lambda p, q: ((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2) ** 0.5
    len_top = lenth(coords['LT'], coords['RT'])
    len_right = lenth(coords['RT'], coords['RB'])
    len_floor = lenth(coords['LB'], coords['RB'])
    len_left = lenth(coords['LT'], coords['LB'])
    return len_top+len_right+len_floor+len_left

#another varient:
# def figure_perimetr(data):
#     a = re.findall(r'([A-Z][A-Z])', data)
#     x_coords = {i + 'x': int(*re.findall(fr'[\w\#:]*{i}(\d)[\w\#:]*', data)) for i in a}
#     y_coords = {i + 'y': int(*re.findall(fr'[\w\#:]*{i}\d:(\d)[\w\#:]*', data)) for i in a}
#     len_top = ((x_coords['RTx'] - x_coords['LTx']) ** 2 + (y_coords['RTy'] - y_coords['LTy']) ** 2) ** 0.5
#     len_right = ((x_coords['RBx'] - x_coords['RTx']) ** 2 + (y_coords['RBy'] - y_coords['RTy']) ** 2) ** 0.5
#     len_floor = ((x_coords['RBx'] - x_coords['LBx']) ** 2 + (y_coords['RBy'] - y_coords['LBy']) ** 2) ** 0.5
#     len_left = ((x_coords['LBx'] - x_coords['LTx']) ** 2 + (y_coords['LBy'] - y_coords['LTy']) ** 2) ** 0.5
#     return len_top + len_right + len_floor + len_left

#Tests


test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
print(figure_perimetr(test1)) #Expect 10.0
test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test2)) #Expect 18.734
