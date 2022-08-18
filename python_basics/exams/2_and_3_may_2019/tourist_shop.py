budget = float(input())
price = 0
counter = 0
money_in_enough = False
while True:
    command = input()
    if command == "Stop":
        money_in_enough = True
        break
    product_price = float(input())
    counter += 1
    if counter % 3 == 0:
        price += product_price / 2
    else:
        price += product_price
    if price > budget:
        break
if money_in_enough:
    print(f"You bought {counter} products for {price:.2f} leva.")
else:
    diff = abs(budget - price)
    print("You don't have enough money!")
    print(f"You need {diff:.2f} leva!")
