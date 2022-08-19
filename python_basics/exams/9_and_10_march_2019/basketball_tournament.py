win_counter = 0
lost_counter = 0
while True:
    command = input()
    if command == "End of tournaments":
        break
    games_number = int(input())
    for games in range(1, games_number + 1):
        desi_team_points = int(input())
        other_team_points = int(input())
        diff = abs(desi_team_points - other_team_points)
        if desi_team_points > other_team_points:
            win_counter += 1
            print(f"Game {games} of tournament {command}: win with {diff} points.")
        else:
            lost_counter += 1
            print(f"Game {games} of tournament {command}: lost with {diff} points.")
print(f"{win_counter / (win_counter + lost_counter) * 100:.2f}% matches win")
print(f"{lost_counter / (win_counter + lost_counter) * 100:.2f}% matches lost")
