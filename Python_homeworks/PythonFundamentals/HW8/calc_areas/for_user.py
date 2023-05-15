from calc_area import*


figure = input("Write your figure: rectangle, triangle or circle: ")

match figure:
    case "circle":
        radius = float(input("Write the radius "))
        print(calc_area(get_circle(radius), figure))
    case "rectangle":
        width = float(input("Write the width"))
        lenth = float(input("Write the lenth"))
        print(calc_area(get_rectangle(width, lenth), figure))
    case "triangle":
        height = float(input("Write the height"))
        width = float(input("Write the width"))
        print(calc_area(get_triangle(height, width), figure))
