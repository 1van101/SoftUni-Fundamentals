from math import pi

type = input()
side_a = float(input())
area = 0
if type == "square":
    area = side_a ** 2
    print(f"{area:.3f}")
elif type == "rectangle":
    side_b = float(input())
    area = side_b * side_a
    print(f"{area:.3f}")
elif type == "circle":
    area = pi * side_a * side_a
    print(f"{area:.3f}")
elif type == "triangle":
    side_h = float(input())
    area = side_a * side_h / 2
    print(f"{area:.3f}")