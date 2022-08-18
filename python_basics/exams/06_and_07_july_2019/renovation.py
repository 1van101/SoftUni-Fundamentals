import math
height = int(input())
width = int(input())

percent_not_painted = int(input())
area = height * width * 4
area_for_painting = area - (area * percent_not_painted / 100)
paint_counter = 0
is_painted = False

command = input()

while command != "Tired!":
    paint_counter += int(command)
    if paint_counter >= area_for_painting:
        is_painted = True
        break
    command = input()
diff = abs(area_for_painting - paint_counter)
if is_painted:
    if area_for_painting == paint_counter:
        print("All walls are painted! Great job, Pesho!")
    elif area_for_painting < paint_counter:
        print(f"All walls are painted and you have {round(diff)} l paint left!")
else:
    print(f"{math.ceil(diff)} quadratic m left." )

# import math
#
# height = int(input())
# width = int(input())
# percent_not_painted = int(input())
# is_tired = False
#
# area = height * width * 4
# area_for_painting = math.ceil(area - (area * percent_not_painted / 100))
#
# while True:
#     paint = input()
#     if paint == "Tired!":
#         is_tired = True
#         break
#     area_for_painting -= int(paint)
#     if area_for_painting < 0:
#         print(f"All walls are painted and you have {abs(area_for_painting)} l paint left!")
#         break
#     elif area_for_painting == 0:
#         print("All walls are painted! Great job, Pesho!")
#         break
# if is_tired:
#     print(f"{area_for_painting} quadratic m left.")


