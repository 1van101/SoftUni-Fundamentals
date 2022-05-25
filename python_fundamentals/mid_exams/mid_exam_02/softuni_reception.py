first_empployee = int(input())
second_empployee = int(input())
third_empployee = int(input())
students = int(input())

total_capacity_of_employees = first_empployee + second_empployee + third_empployee
hours_counter = 0

while students > 0:
    hours_counter += 1
    if hours_counter % 4 == 0:
        hours_counter += 1
    students -= total_capacity_of_employees

print(f"Time needed: {hours_counter}h.")