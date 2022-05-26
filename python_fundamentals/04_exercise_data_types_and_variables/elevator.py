people = int(input())
capacity = int(input())
if capacity != 0:
    full_courses = people // capacity
    people_left = people % capacity

    if people_left > 0:
        print(full_courses + 1)
    else:
        print(full_courses + people_left)
else:
    print(0)
