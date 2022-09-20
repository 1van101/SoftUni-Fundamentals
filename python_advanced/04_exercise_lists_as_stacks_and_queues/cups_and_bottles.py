from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]

wasted_water = 0

while cups and bottles:
    current_cup = cups[0]
    current_bottle = bottles.pop()
    if current_cup - current_bottle <= 0:
        wasted_water += current_bottle - cups.popleft()
    else:
        cups[0] -= current_bottle

if bottles:
    print(f"Bottles: {' '.join([str(x) for x in bottles[::-1]])}")
if cups:
    print(f"Cups: {' '.join([str(x) for x in cups])}")
print(f"Wasted litters of water: {wasted_water}")