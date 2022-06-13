def add_lesson(command, courses):
    add_lesson = command[1]
    if add_lesson not in courses:
        courses.append(add_lesson)
    return courses


def insert_lesson(command, courses):
    insert_lesson = command[1]
    index = int(command[2])
    if index <= len(courses) and index >= 0:
        if insert_lesson not in courses:
            courses.insert(index, insert_lesson)
        return courses
    return courses


def remove_lesson(command, courses):
    remove_lesson = command[1]
    if f"{remove_lesson}-Exercise" in courses:
        courses.remove(f"{remove_lesson}-Exercise")
    if remove_lesson in courses:
        courses.remove(remove_lesson)
    return courses


def swap_lessons(command, courses):
    if f"{command[1]}-Exercise" in courses and f"{command[2]}-Exercise" in courses:
        swap_ex_first_lesson_index = courses.index(f"{command[1]}-Exercise")
        swap_ex_second_lesson_index = courses.index(f"{command[2]}-Exercise")
        courses[swap_ex_first_lesson_index], courses[swap_ex_second_lesson_index] = courses[
                                                                                        swap_ex_second_lesson_index], \
                                                                                    courses[
                                                                                        swap_ex_first_lesson_index]
    elif f"{command[1]}-Exercise" in courses:
        pop_item = courses.pop(courses.index(f"{command[1]}-Exercise"))
        courses.insert(courses.index(command[1]) + 1, pop_item)
    elif f"{command[2]}-Exercise" in courses:
        pop_item = courses.pop(courses.index(f"{command[2]}-Exercise"))
        courses.insert(courses.index(command[1]) + 1, pop_item)

    if command[1] in courses and command[2] in courses:
        swap_first_lesson_index = courses.index(command[1])
        swap_second_lesson_index = courses.index(command[2])
        courses[swap_first_lesson_index], courses[swap_second_lesson_index] = courses[swap_second_lesson_index], \
                                                                              courses[swap_first_lesson_index]
    return courses


def add_exercise(command, courses):
    exercise_lesson = command[1]
    if exercise_lesson in courses:
        if f"{exercise_lesson}-Exercise" not in courses:
            courses.insert(courses.index(exercise_lesson) + 1, f"{exercise_lesson}-Exercise")
    else:
        courses.append(exercise_lesson)
        courses.append(f"{exercise_lesson}-Exercise")
    return courses


courses = input().split(", ")
current_command = input()

while current_command != "course start":
    current_command = current_command.split(":")
    action = current_command[0]
    if action == "Add":
        courses = add_lesson(current_command, courses)
    elif action == "Insert":
        courses = insert_lesson(current_command, courses)
    elif action == "Remove":
        courses = remove_lesson(current_command, courses)
    elif action == "Swap":
        courses = swap_lessons(current_command, courses)
    elif action == "Exercise":
        courses = add_exercise(current_command, courses)

    current_command = input()

for i in range(1, len(courses) + 1):
    print(f"{i}.{courses[i - 1]}")
