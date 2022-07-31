actor = input()
points_of_academy = float(input())
jury_number = int(input())

actor_points = points_of_academy

for i in range(1, jury_number + 1):
    name_of_jury = input()
    points_of_jury = float(input())
    lenght_name_of_jury = len(name_of_jury)
    total_points = lenght_name_of_jury * points_of_jury / 2
    actor_points = actor_points + total_points
    if actor_points > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {actor_points:.1f}!")
        break
if actor_points <= 1250.5:
    difference = 1250.5 - actor_points
    print(f"Sorry, {actor} you need {difference:.1f} more!")

# name = input()
# academy_points = float(input())
# number_of_jury = int(input())
#
# is_nominated = False
#
# for i in range(1, number_of_jury + 1):
#     jury_name = input()
#     jury_points = float(input())
#
#     jury_name_lenght = len(jury_name)
#     points_counter = jury_name_lenght * jury_points / 2
#     academy_points += points_counter
#
#     if academy_points >= 1250.5:
#         is_nominated = True
#         break
#
# if is_nominated:
#     print(f"Congratulations, {name} got a nominee for leading role with {academy_points:.1f}!")
# else:
#     diff = 1250.5 - academy_points
#     print(f"Sorry, {name} you need {diff:.1f} more!")
