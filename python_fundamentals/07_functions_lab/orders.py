def total_price_calculation(type, qty):
    price = 0
    if type == "coffee":
        price = 1.5
    elif type == "water":
        price = 1
    elif type == "coke":
        price = 1.4
    elif type == "snacks":
        price = 2
    return price * qty


type_of_drink = input()
quantity = int(input())
result = total_price_calculation(type_of_drink, quantity)
print(f"{result:.2f}")

