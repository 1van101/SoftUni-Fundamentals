number_balls = int(input())

total_points = 0
red_counter = 0
orange_counter = 0
yellow_counter = 0
white_counter = 0
other_counter = 0
black_counter = 0

for balls in range(number_balls):
    color = input()
    if color == "red":
        total_points += 5
        red_counter += 1
    elif color == "orange":
        total_points += 10
        orange_counter += 1
    elif color == "yellow":
        total_points += 15
        yellow_counter += 1
    elif color == "white":
        total_points += 20
        white_counter += 1
    elif color == "black":
        total_points = total_points // 2
        black_counter += 1
    else:
        other_counter += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red_counter}")
print(f"Orange balls: {orange_counter}")
print(f"Yellow balls: {yellow_counter}")
print(f"White balls: {white_counter}")
print(f"Other colors picked: {other_counter}")
print(f"Divides from black balls: {black_counter}")



