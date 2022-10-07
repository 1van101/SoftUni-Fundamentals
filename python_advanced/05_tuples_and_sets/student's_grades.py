num = int(input())

students_info = {}
for _ in range(num):
    current_name, current_grade = input().split()
    try:
        students_info[current_name].append(float(current_grade))
    except KeyError:
        students_info[current_name] = [float(current_grade)]

for name in students_info.keys():
    grades_unpacked = ' '.join([f'{x:.2f}' for x in students_info[name]])
    print(f"{name} -> {grades_unpacked} (avg: {sum(students_info[name]) / len(students_info[name]):.2f})")

# PRINT WITH COMPREHENSION -> [
# print(f"{x} -> {' '.join([str(f'{el:.2f}') for el in y])} (avg: {sum(y) / len(y):.2f})")
# for x, y in students_info.items()
# ]
