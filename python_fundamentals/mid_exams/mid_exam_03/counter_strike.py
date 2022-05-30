initial_energy = int(input())
battles_won = 0
is_out_of_energy = False

command = input()

while command != "End of battle":
    command = int(command)

    if initial_energy - command < 0:
        is_out_of_energy = True
        break
    else:
        initial_energy -= command
        battles_won += 1
        if battles_won % 3 == 0:
            initial_energy += battles_won

    command = input()

if is_out_of_energy:
    print(f"Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy")
else:
    print(f"Won battles: {battles_won}. Energy left: {initial_energy}")
