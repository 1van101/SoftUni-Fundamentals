number_of_students = int(input())

s1 = 0
s2 = 0
s3 = 0
s4 = 0
grades_sum = 0
for students in range(number_of_students):
    students_grades = float(input())
    grades_sum += students_grades
    if students_grades >= 5.00:
        s1 += 1
    elif students_grades >= 4.00:
        s2 += 1
    elif students_grades >= 3.00:
        s3 += 1
    else:
        s4 += 1

average_grades = grades_sum / number_of_students
s1_percent = s1 / number_of_students * 100
s2_percent = s2 / number_of_students * 100
s3_percent = s3 / number_of_students * 100
s4_percent = s4 / number_of_students * 100

print(f"Top students: {s1_percent:.2f}%")
print(f"Between 4.00 and 4.99: {s2_percent:.2f}%")
print(f"Between 3.00 and 3.99: {s3_percent:.2f}%")
print(f"Fail: {s4_percent:.2f}%")
print(f"Average: {average_grades:.2f}")