rooms = int(input())
counter = 0
free_chairs = []

for number_room in range(1, rooms + 1):
    chairs_and_visitors = input().split()
    chairs_number = len(chairs_and_visitors[0])
    visitors_number = int(chairs_and_visitors[1])
    diff = abs(visitors_number - chairs_number)
    if chairs_number < visitors_number:
        print(f"{diff} more chairs needed in room {number_room}")
    else:
        free_chairs.append(diff)
        counter += 1

if counter == rooms:
    print(f"Game On, {sum(free_chairs)} free chairs left")

