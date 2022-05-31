def current_position_determining(houses, jump_lenght, position):
    position += jump_lenght
    if position >= len(houses):
        position = 0
    return position


def jump(houses, cur_pos):
    if houses[cur_pos] == 0:
        print(f"Place {cur_pos} already had Valentine's day.")
        return houses
    houses[cur_pos] -= 2
    if houses[cur_pos] == 0:
        print(f"Place {cur_pos} has Valentine's day.")
    return houses


neighborhood_houses = [int(x) for x in input().split("@")]
command = input()

current_position = 0

while command != "Love!":
    command = command.split()
    jump_lenght = int(command[1])

    current_position = current_position_determining(neighborhood_houses, jump_lenght, current_position)
    neighborhood_houses = jump(neighborhood_houses, current_position)

    command = input()
print(f"Cupid's last position was {current_position}.")
failed_houses = [x for x in neighborhood_houses if x != 0]

if len(failed_houses) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(failed_houses)} places.")
