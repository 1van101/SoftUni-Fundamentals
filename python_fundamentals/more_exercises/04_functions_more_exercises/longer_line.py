def length_of_line(x1, y1, x2, y2):
    return ((x2 - x1) ** 2) + ((y2 - y1) ** 2)

def closer_point_to_center(x1, y1, x2, y2):
    if x1 ** 2 + y1 ** 2 > x2 ** 2 + y2 ** 2:
        return f"({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})"
    else:
        return f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})"

first_x = float(input())
first_y = float(input())
second_x = float(input())
second_y = float(input())
third_x = float(input())
third_y = float(input())
fourth_x = float(input())
fourth_y = float(input())

if length_of_line(first_x, first_y, second_x, second_y) >= length_of_line(third_x, third_y, fourth_x, fourth_y):
    print(closer_point_to_center(first_x, first_y, second_x, second_y))
else:
    print(closer_point_to_center(third_x, third_y, fourth_x, fourth_y))
