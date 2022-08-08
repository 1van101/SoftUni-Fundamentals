num = int(input())
final_assessment = 0
projects_counter = 0
while True:
    project_name = input()
    project_grades_sum = 0
    if project_name == "Finish":
        break
    projects_counter += 1
    for project in range(num):
        grade = float(input())
        project_grades_sum += grade

    project_average_grade = project_grades_sum / num
    final_assessment += project_average_grade
    print(f"{project_name} - {project_average_grade:.2f}.")
final_assessment /= projects_counter
print(f"Student's final assessment is {final_assessment:.2f}.")
