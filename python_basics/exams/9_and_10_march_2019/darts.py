player_name = input()
shots_counter = 0
unsuccesful_shots_counter = 0
points = 301
current_points_counter = 0
is_retire = False
is_won = False

while True:
    command = input()
    if command == "Retire":
        is_retire = True
        break
    current_points = int(input())
    if command == "Single":
        current_points_counter = current_points
        points -= current_points
    elif command == "Double":
        current_points_counter = current_points * 2
        points -= current_points * 2
    else:
        current_points_counter = current_points * 3
        points -= current_points * 3
    if points < 0:
        unsuccesful_shots_counter += 1
        points += current_points_counter
        continue
    shots_counter += 1
    if points == 0:
        is_won = True
        break

if is_won:
    print(f"{player_name} won the leg with {shots_counter} shots.")
elif is_retire:
    print(f"{player_name} retired after {unsuccesful_shots_counter} unsuccessful shots.")


