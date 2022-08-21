command = input()
goals = int(input())

is_valid = False
hat_trick = False
player = command
num_goals = goals
while command != "END":
    if num_goals >= 3:
        hat_trick = True
        if num_goals >= 10:
            is_valid = True
            break

    current_command = input()
    if current_command == "END":
        break
    current_goals = int(input())
    if current_goals > num_goals:
        num_goals = current_goals
        player = current_command

print(f"{player} is the best player!")
if hat_trick or is_valid:
    print(f"He has scored {num_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {num_goals} goals.")





