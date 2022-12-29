from collections import deque

orders = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]

total_pizzas = sum([x for x in orders if x in range(0, 11)])

while orders and employees:
    current_order = orders.popleft()
    if current_order <= 0 or current_order > 10:
        continue
    current_employee = employees.pop()

    if current_order > current_employee:
        orders.appendleft(current_order - current_employee)

if orders:
    print(f"Not all orders are completed.\nOrders left: {', '.join(str(x) for x in orders)}")
else:
    print(f"All orders are successfully completed!\nTotal pizzas made: {total_pizzas}")
    if employees:
        print(f"Employees: {', '.join(str(x) for x in employees)}")
