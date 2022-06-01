from math import ceil

students_number = int(input())
lectures_number = int(input())
additional_bonus = int(input())

max_bonus = 0
attendances = 0

for student in range(students_number):
    current_student_attendances = int(input())
    current_bonus = current_student_attendances / lectures_number * (5 + additional_bonus)
    if current_bonus > max_bonus:
        max_bonus = current_bonus
        attendances = current_student_attendances

print(f"Max Bonus: {ceil(max_bonus)}.\nThe student has attended {attendances} lectures.")
