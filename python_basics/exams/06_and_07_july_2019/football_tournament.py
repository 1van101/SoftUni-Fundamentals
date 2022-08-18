team = input()
games_number = int(input())
points_counter = 0
w_counter = 0
d_counter = 0
l_counter = 0

for games in range(games_number):
    result = input()
    if result == "W":
        w_counter += 1
        points_counter += 3
    elif result == "D":
        d_counter += 1
        points_counter += 1
    else:
        l_counter += 1

if games_number < 1:
    print(f"{team} hasn't played any games during this season.")
else:
    print(f"{team} has won {points_counter} points during this season.")
    print("Total stats:")
    print(f"## W: {w_counter}")
    print(f"## D: {d_counter}")
    print(f"## L: {l_counter}")
    print(f"Win rate: {w_counter / games_number * 100:.2f}%")