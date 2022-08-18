budget = float(input())
fuel_needed = float(input())
day_of_week = input()
fuel_needed_price = 2.1 * fuel_needed + 100
total_price = 0
if day_of_week == "Saturday":
    total_price = fuel_needed_price * 0.9
else:
    total_price = fuel_needed_price * 0.8

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")