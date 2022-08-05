room_width = int(input())
room_lenght = int(input())
room_height = int(input())

room_volume = room_height * room_lenght * room_width
cartons_counter = 0

room_is_full = False

command = input()

while room_volume > cartons_counter:
    if command == "Done":
        break

    cartons_counter += int(command)

    if room_volume <= cartons_counter:
        room_is_full = True
        break
    command = input()

difference = abs(room_volume - cartons_counter)

if room_is_full:
    print(f"No more free space! You need {difference} Cubic meters more.")
else:
    print(f"{difference} Cubic meters left.")