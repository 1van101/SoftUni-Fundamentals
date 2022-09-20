from collections import deque

green_light_duration = int(input())
free_window = int(input())
cars = deque()
passed_cars = []
while True:
    current_green_light = green_light_duration
    current_free_window = free_window
    command = input()
    if command == "END":
        break
    if command == "green":
        while current_free_window >= 0 and cars:
            if current_green_light > 0:
                current_car = cars.popleft()
                if len(current_car) > current_green_light:
                    if len(current_car) > current_green_light + current_free_window:
                        character_hit = current_car[current_green_light + current_free_window]
                        print(f"A crash happened!\n{current_car} was hit at {character_hit}.")
                        exit()
                    else:
                        current_free_window -= (len(current_car) - current_green_light)
                        passed_cars.append(current_car)
                        current_green_light = 0
                else:
                    current_green_light -= len(current_car)
                    passed_cars.append(current_car)
            else:
                if len(cars[0]) <= current_free_window:
                    passed_cars.append(cars.popleft())
                else:
                    break
    else:
        cars.append(command)

print(f"Everyone is safe.\n{len(passed_cars)} total cars passed the crossroads.")
