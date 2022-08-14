game_moves = int(input())

total_points = 0
nums_0_to_9 = 0
nums_10_to_19 = 0
nums_20_to_29 = 0
nums_30_to_39 = 0
nums_40_to_50 = 0
invalid_nums = 0

for moves in range (game_moves):
    points = int(input())

    if 0 <= points <= 9:
        total_points += 0.2 * points
        nums_0_to_9 += 1
    elif 10 <= points <= 19:
        total_points += 0.3 * points
        nums_10_to_19 += 1
    elif 20 <= points <= 29:
        total_points += 0.4 * points
        nums_20_to_29 += 1
    elif 30 <= points <= 39:
        total_points += 50
        nums_30_to_39 += 1
    elif 40 <= points <= 50:
        total_points += 100
        nums_40_to_50 += 1
    elif points > 50 or points < 0:
        invalid_nums += 1
        total_points /= 2

nums_0_to_9_percent = nums_0_to_9 / game_moves * 100
nums_10_to_19_percent = nums_10_to_19/ game_moves * 100
nums_20_to_29_percent = nums_20_to_29 / game_moves * 100
nums_30_to_39_percent = nums_30_to_39 / game_moves * 100
nums_40_to_50_percent = nums_40_to_50 / game_moves * 100
invalid_nums_percent = invalid_nums / game_moves * 100

print(f"{total_points:.2f}")
print(f"From 0 to 9: {nums_0_to_9_percent:.2f}%")
print(f"From 10 to 19: {nums_10_to_19_percent:.2f}%")
print(f"From 20 to 29: {nums_20_to_29_percent:.2f}%")
print(f"From 30 to 39: {nums_30_to_39_percent:.2f}%")
print(f"From 40 to 50: {nums_40_to_50_percent:.2f}%")
print(f"Invalid numbers: {invalid_nums_percent:.2f}%")