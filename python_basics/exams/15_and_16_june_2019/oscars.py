actor_name = input()
points = float(input())
number_of_judges = int(input())
is_nominated = False

for i in range(number_of_judges):
    name_of_judge = input()
    points_of_judge = float(input())
    points = points + (len(name_of_judge) * points_of_judge/ 2)
    if points > 1250.5:
        is_nominated = True
        break

if is_nominated:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - points:.1f} more!")
