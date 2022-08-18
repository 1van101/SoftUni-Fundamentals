drink = input()
sweet = input()
num_of_drinks = int(input())
price = 0
if drink == "Espresso":
    if sweet == "Without":
        price = 0.9 * 0.65
    elif sweet == "Normal":
        price = 1
    elif sweet == "Extra":
        price = 1.2
    if num_of_drinks >= 5:
        price *= 0.75
elif drink == "Cappuccino":
    if sweet == "Without":
        price = 1 * 0.65
    elif sweet == "Normal":
        price = 1.2
    elif sweet == "Extra":
        price = 1.6
elif drink == "Tea":
    if sweet == "Without":
        price = 0.5 * 0.65
    elif sweet == "Normal":
        price = 0.6
    elif sweet == "Extra":
        price = 0.7

total_price = price * num_of_drinks
if total_price > 15:
    total_price *= 0.8

print(f"You bought {num_of_drinks} cups of {drink} for {total_price:.2f} lv.")
