from collections import deque

operations = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y
}

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

collected_honey = 0

while bees and nectar:
    current_bee = bees[0]
    current_nectar = nectar.pop()
    if current_nectar < current_bee:
        continue
    current_operator = symbols.popleft()
    current_bee = bees.popleft()
    try:
        collected_honey += (abs(operations[current_operator](current_bee,current_nectar)))
    except ZeroDivisionError:
        pass

print(f"Total honey made: {collected_honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")