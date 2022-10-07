from collections import deque

chocolate = [int(x) for x in input().split(", ")]
milk_cups = deque([int(x) for x in input().split(", ")])

milkshakes = 0
milkshakes_ready = False
while milk_cups and chocolate:

    current_milk_cup = milk_cups[0]
    current_chocolate = chocolate[-1]
    if current_chocolate <= 0 or current_milk_cup <= 0:
        if current_chocolate <= 0:
            chocolate.pop()
        if current_milk_cup <= 0:
            milk_cups.popleft()
        continue
    if current_chocolate == current_milk_cup:
        milkshakes += 1
        milk_cups.popleft()
        chocolate.pop()
    else:
        milk_cups.append(milk_cups.popleft())
        chocolate[-1] -= 5

    if milkshakes == 5:
        milkshakes_ready = True
        break

if milkshakes_ready:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join([str(x) for x in milk_cups])}")
else:
    print("Milk: empty")