number_of_easter_breads = int(input())
the_best_baker = ""
max_points = 0

for easter_breads in range(number_of_easter_breads):
    current_points_sum = 0
    baker_name = input()
    while True:
        current_points = input()

        if current_points == "Stop":
            print(f"{baker_name} has {current_points_sum} points.")
            break
        current_points_sum += int(current_points)
    if current_points_sum > max_points:
        max_points = current_points_sum
        the_best_baker = baker_name
        print(f"{baker_name} is the new number 1!")
print(f"{the_best_baker} won competition with {max_points} points!")

