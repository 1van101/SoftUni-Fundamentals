import math

days = int(input())
food_left_kg = int(input())
food_for_dog_kg = float(input())
food_for_cat_kg = float(input())
food_for_turtle_gr = float(input())

food_needed = (food_for_dog_kg + food_for_cat_kg + food_for_turtle_gr / 1000) * days
difference = abs(food_left_kg - food_needed)
if food_left_kg >= food_needed:
    print (f"{math.floor(difference)} kilos of food left.")
else:
    print(f"{math.ceil(difference)} more kilos of food are needed.")