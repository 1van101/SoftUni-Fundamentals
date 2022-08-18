number_games = int(input())
hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0

for games in range (number_games):
    current_game = input()
    if current_game == "Hearthstone":
        hearthstone_counter += 1
    elif current_game == "Fornite":
        fornite_counter += 1
    elif current_game == "Overwatch":
        overwatch_counter += 1
    else:
        others_counter += 1
print(f"Hearthstone - {hearthstone_counter / number_games * 100:.2f}%")
print(f"Fornite - {fornite_counter / number_games * 100:.2f}%")
print(f"Overwatch - {overwatch_counter / number_games * 100:.2f}%")
print(f"Others - {others_counter / number_games * 100:.2f}%")