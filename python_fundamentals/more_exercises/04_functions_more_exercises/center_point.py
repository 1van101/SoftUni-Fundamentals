import math


def get_closest_to_the_center_point(x1, y1, x2, y2):
    if abs(x1) + abs(y1) > abs(x2) + abs(y2):
        return f"({math.floor(x2)}, {math.floor(y2)})"
    elif (abs(x1) + abs(y1) < abs(x2) + abs(y2)) or (abs(x1) + abs(y1) == abs(x2) + abs(y2)):
        return f"({math.floor(x1)}, {math.floor(y1)})"


first_x = float(input())
second_x = float(input())
first_y = float(input())
second_y = float(input())
print(get_closest_to_the_center_point(first_x, second_x, first_y, second_y))