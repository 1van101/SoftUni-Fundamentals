steps_goal = 10000
command = input()

steps_sum = 0
goal_reached = False
while steps_sum < steps_goal:
    if command == "Going home":
        command = int(input())
        steps_sum += command
        if steps_sum > steps_goal:
            goal_reached = True
        break
    steps_sum += int(command)
    if steps_sum >= steps_goal:
        goal_reached = True
        break


    command = input()
difference = abs(steps_goal - steps_sum)
if goal_reached == True:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
# goal = 10000
# steps_counter = 0
#
# is_goal_reached = False
#
# while goal > steps_counter:
#     command = input()
#     if command == "Going home":
#         command = int(input())
#         steps_counter += command
#         if steps_counter >= goal:
#             is_goal_reached = True
#         break
#     steps_counter += int(command)
#     if steps_counter >= goal:
#         is_goal_reached = True
# diff = abs(goal - steps_counter)
# if is_goal_reached:
#     print("Goal reached! Good job!")
#     print(f"{diff} steps over the goal!")
# else:
#     print(f"{diff} more steps to reach goal.")