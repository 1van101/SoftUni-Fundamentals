name_student = input()

grades_sum = 0
years = 1
fail_counter = 0
while years <= 12:
    if fail_counter > 1:
        break
    grade = float(input())
    if grade < 4:
        fail_counter += 1
        continue
    grades_sum += grade
    years += 1

average_grade = grades_sum / 12

if fail_counter > 1:
    print(f"{name_student} has been excluded at {years} grade")
else:
    print(f"{name_student} graduated. Average grade: {average_grade:.2f}")

# name = input()
# fail_counter = 0
# grade = 1
# annual_grades_sum = 0
# is_excluded = False
# while grade <= 12:
#     if fail_counter == 2:
#         is_excluded = True
#         break
#     annual_grade = float(input())
#     if annual_grade < 4:
#         fail_counter += 1
#         continue
#     grade += 1
#     annual_grades_sum += annual_grade
#
# average_grade = annual_grades_sum / 12
# if is_excluded:
#     print(f"{name} has been excluded at {grade} grade")
# else:
#     print(f"{name} graduated. Average grade: {average_grade:.2f}")

