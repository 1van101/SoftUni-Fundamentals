from collections import deque

pumps = int(input())
que_with_pumps = deque()

for _ in range(pumps):
    value = [int(x) for x in input().split()]
    que_with_pumps.append(value)

for attempt in range(len(que_with_pumps)):
    current_fuel = 0
    failed = False
    for fuel, distance in que_with_pumps:
        current_fuel += fuel
        if current_fuel < distance:
            failed = True
            break
        current_fuel -= distance

    if failed:
        que_with_pumps.rotate(-1)
    else:
        print(attempt)
        break