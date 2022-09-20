from collections import deque

food_qty = int(input())
orders = deque([int(x) for x in input().split()])
print(max(orders))

while orders:
    current_order = orders[0]
    if food_qty - current_order < 0:
        break
    food_qty -= orders.popleft()

if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
else:
    print("Orders complete")