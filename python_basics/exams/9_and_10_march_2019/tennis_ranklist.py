number_of_tournaments = int(input())
inital_points_in_ranglist = int(input())

points = 0
tournaments_won = 0

for tournament in range(number_of_tournaments):
    progress_in_tournament = input()
    if progress_in_tournament == "W":
        points += 2000
        tournaments_won += 1
    elif progress_in_tournament == "F":
        points += 1200
    elif progress_in_tournament == "SF":
        points += 720

points_total = inital_points_in_ranglist + points
average_points = points // number_of_tournaments
tournaments_won_percent = tournaments_won / number_of_tournaments * 100
print(f"Final points: {points_total}")
print(f"Average points: {average_points}")
print(f"{tournaments_won_percent:.2f}%")
