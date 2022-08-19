visitors = int(input())
back_workout = 0
chest_workout = 0
legs_workout = 0
abs_workout = 0
protein_shakes_counter = 0
protein_bars_counter = 0
for people in range(visitors):
    activity = input()
    if activity == "Back":
        back_workout += 1
    elif activity == "Chest":
        chest_workout += 1
    elif activity == "Legs":
        legs_workout += 1
    elif activity == "Abs":
        abs_workout += 1
    elif activity == "Protein shake":
        protein_shakes_counter += 1
    else:
        protein_bars_counter += 1
workout_visitors = back_workout + chest_workout + legs_workout + abs_workout
protein_buyers = protein_bars_counter + protein_shakes_counter
print(f"{back_workout} - back")
print(f"{chest_workout} - chest")
print(f"{legs_workout} - legs")
print(f"{abs_workout} - abs")
print(f"{protein_shakes_counter} - protein shake")
print(f"{protein_bars_counter} - protein bar")
print(f"{workout_visitors / visitors * 100:.2f}% - work out")
print(f"{protein_buyers / visitors * 100:.2f}% - protein")