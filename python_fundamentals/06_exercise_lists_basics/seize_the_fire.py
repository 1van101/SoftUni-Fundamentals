level_of_fire = input().split("#")
amount_of_water = int(input())

cells = []
total_fire = 0

for level in level_of_fire:
    level = level.split(" = ")
    level_num = int(level[1])
    type_of_fire = level[0]
    if type_of_fire == "High" and 81 <= level_num <= 125:
        total_fire += level_num
        cells.append(level_num)
    elif type_of_fire == "Medium" and 51 <= level_num <= 80:
        total_fire += level_num
        cells.append(level_num)
    elif type_of_fire == "Low" and 1 <= level_num <= 50:
        total_fire += level_num
        cells.append(level_num)
    if total_fire > amount_of_water:
        total_fire -= level_num
        cells.remove(level_num)
effort = total_fire / 4
print("Cells:")
for i in cells:
    print(f"- {i}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")




