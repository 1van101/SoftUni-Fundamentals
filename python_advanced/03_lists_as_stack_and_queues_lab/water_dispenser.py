from collections import deque

qty_of_water = int(input())
some_people = deque()

while True:
    name = input()
    if name == "Start":
        break
    some_people.append(name)

while True:
    command = input().split()
    if "End" in command:
        break
    if command[0] == "refill":
        qty_of_water += int(command[1])
    else:
        liters = int(command[0])
        if liters <= qty_of_water:
            qty_of_water -= liters
            print(f"{some_people.popleft()} got water")
        else:
            print(f"{some_people.popleft()} must wait")

print(f"{qty_of_water} liters left")
