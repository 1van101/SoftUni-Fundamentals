rooms = int(input())

is_enough_chairs = True
free_chairs = []

for room in range(1, rooms + 1):
    data = input().split()
    chairs = len(data[0])
    visitors = int(data[1])
    free_chairs.append(chairs - visitors)

    if chairs < visitors:
        is_enough_chairs = False
        print(f"{visitors - chairs} more chairs needed in room {room}")

if is_enough_chairs:
    print(f"Game On, {sum(free_chairs)} free chairs left")
