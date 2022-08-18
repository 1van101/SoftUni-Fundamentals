points_counter = 0
player = ""

while True:
    command = input()
    if command == "Stop":
        break
    current_points_counter = 0
    for char, symbol in enumerate(command):
        current_points = int(input())
        if ord(symbol) == current_points:
            current_points_counter += 10
        else:
            current_points_counter += 2
    if current_points_counter >= points_counter:
        points_counter = current_points_counter
        player = command
print(f"The winner is {player} with {points_counter} points!")
