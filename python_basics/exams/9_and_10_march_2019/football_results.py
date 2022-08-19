first_game_result = input()
second_game_result = input()
third_game_result = input()
won_counter = 0
lost_counter = 0
drawn_counter = 0
if first_game_result[0] > first_game_result[2]:
    won_counter += 1
elif first_game_result[0] == first_game_result[2]:
    drawn_counter += 1
else:
    lost_counter += 1
if second_game_result[0] > second_game_result[2]:
    won_counter += 1
elif second_game_result[0] == second_game_result[2]:
    drawn_counter += 1
else:
    lost_counter += 1
if third_game_result[0] > third_game_result[2]:
    won_counter += 1
elif third_game_result[0] == third_game_result[2]:
    drawn_counter += 1
else:
    lost_counter += 1
print(f"Team won {won_counter} games.")
print(f"Team lost {lost_counter} games.")
print(f"Drawn games: {drawn_counter}")