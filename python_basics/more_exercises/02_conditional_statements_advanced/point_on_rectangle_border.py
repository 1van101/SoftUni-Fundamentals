x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

is_valid = True


if x1 < x2 and y1 < y2:
    is_valid = is_valid
else:
    is_valid = False

if is_valid:
    if (x == x1 or x == x2) and y1 <= y <= y2:
        print("Border")
    elif (y == y1 or y == y2) and x1 <= x <= x2:
        print("Border")
    else:
        print("Inside / Outside")
else:
    pass