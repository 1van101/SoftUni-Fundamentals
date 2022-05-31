food_qty = float(input())
hay = float(input())
cover = float(input())
guinea_pig_weight = float(input())

is_out_of_food = False
food_in_grams = food_qty * 1000
hay_in_grams = hay * 1000
cover_in_grams = cover * 1000
guinea_pig_weight_in_grams = guinea_pig_weight * 1000
for day in range(1, 31):
    food_in_grams -= 300
    if day % 2 == 0:
        hay_in_grams -= (0.05 * food_in_grams)
    if day % 3 == 0:
        cover_in_grams -= (guinea_pig_weight_in_grams / 3)
    if food_in_grams <= 0 or hay_in_grams <= 0 or cover_in_grams <= 0:
        is_out_of_food = True
        break

if is_out_of_food:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_in_grams / 1000:.2f}, Hay: {hay_in_grams / 1000:.2f}, Cover: {cover_in_grams / 1000:.2f}.")