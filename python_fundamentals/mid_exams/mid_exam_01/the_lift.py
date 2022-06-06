number_of_people = int(input())
current_lift_space = [int(x) for x in input().split()]

for i in range(len(current_lift_space)):
    current_loading_capacity = min(4 - current_lift_space[i], number_of_people)
    number_of_people -= current_loading_capacity
    current_lift_space[i] += current_loading_capacity

empty_spots = False
for i in current_lift_space:
    if i != 4:
        empty_spots = True

current_lift_space = [str(x) for x in current_lift_space]
if empty_spots:
    print("The lift has empty spots!")
else:
    if number_of_people != 0:
        print(f"There isn't enough space! {number_of_people} people in a queue!")

print(f"{' '.join(current_lift_space)}")
