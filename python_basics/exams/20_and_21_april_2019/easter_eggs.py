eggs_num = int(input())
red = 0
orange = 0
blue = 0
green = 0
max_num_eggs_color = ""

for eggs in range(eggs_num):

    egg_color = input()
    if egg_color == "red":
        red += 1
    elif egg_color == "orange":
        orange += 1
    elif egg_color == "blue":
        blue += 1
    elif egg_color == "green":
        green += 1

list = [red, orange, blue, green]

if max(list) == red:
    max_num_eggs_color = "red"
elif max(list) == orange:
    max_num_eggs_color = "orange"
elif max(list) == blue:
    max_num_eggs_color = "blue"
elif max(list) == green:
    max_num_eggs_color = "green"

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max(list)} -> {max_num_eggs_color}")