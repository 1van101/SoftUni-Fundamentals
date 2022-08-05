low_grades_number = int(input())
low_grades_counter = 0
all_grades_sum = 0
all_problems_sum = 0
name_of_problem = input()
current_grade = int(input())
is_bad_student = False
last_problem = ""
while name_of_problem != "Enough":
    if current_grade <= 4:
        low_grades_counter += 1
    if low_grades_counter == low_grades_number:
        is_bad_student = True
        break
    all_grades_sum += current_grade
    all_problems_sum += 1
    name_of_problem = input()
    if name_of_problem == "Enough":
        break
    current_grade = int(input())
    last_problem = name_of_problem

if is_bad_student:
    print(f"You need a break, {low_grades_counter} poor grades.")
else:
    average_score = all_grades_sum / all_problems_sum
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {all_problems_sum}")
    print(f"Last problem: {last_problem}")

# poor_grades_allowed = int(input())
# last_problem = ""
# poor_grades_counter = 0
# problems_counter = 0
# grades_sum = 0
# is_excluded = False
# command = input()
# while command != "Enough":
#     grade = int(input())
#     problems_counter += 1
#     grades_sum += grade
#     if grade <= 4:
#         poor_grades_counter += 1
#     if poor_grades_counter == poor_grades_allowed:
#         is_excluded= True
#         break
#
#     last_problem = command
#     command = input()
#
# average_score = grades_sum / problems_counter
#
# if is_excluded:
#     print(f"You need a break, {poor_grades_counter} poor grades.")
# else:
#     print(f"Average score: {average_score:.2f}")
#     print(f"Number of problems: {problems_counter}")
#     print(f"Last problem: {last_problem}")