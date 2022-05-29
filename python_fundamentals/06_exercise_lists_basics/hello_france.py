ticket = 150
collection_of_items = input().split("|")
budget = int(input())

total_sum = 0
sold_list = []

for item in collection_of_items:
    item = item.split("->")
    type = item[0]
    price = float(item[1])
    if type == "Clothes" and 0 <= price <= 50:
        total_sum += price
        sold_list.append(price)
    elif type == "Shoes" and 0 <= price <= 35:
        total_sum += price
        sold_list.append(price)
    elif type == "Accessories" and 0 <= price <= 20.50:
        total_sum += price
        sold_list.append(price)
    if total_sum > budget:
        total_sum -= price
        sold_list.remove(price)
for new_price in sold_list:
    print(f"{new_price * 1.4:.2f}", end=" ")
print()
profit = total_sum * 0.4
print(f"Profit: {profit:.2f}")

if (budget - total_sum) + total_sum + profit >= ticket:
    print("Hello, France!")
else:
    print("Not enough money.")

