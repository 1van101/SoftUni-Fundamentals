students = {}
searched_course = None

while True:
    current_input = input()

    if ":" not in current_input:
        searched_course = current_input
        break

    current_args = current_input.split(":")
    name = current_args[0]
    id = current_args[1]
    course = current_args[2]

    if name not in students:
        students[name] = {}

    students[name][id] = course

searched_course = searched_course.replace("_", " ")

for k, v in students.items():
    for nested_k, nested_v in v.items():
        if nested_v == searched_course:
            print(f"{k} - {nested_k}")
