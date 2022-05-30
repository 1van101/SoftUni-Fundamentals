list_of_products = {}
while True:
    command = input().split(": ")
    if "statistics" in command:
        break

    product = command[0]
    qty = int(command[1])

    if product not in list_of_products:
        list_of_products[product] = qty
    else:
        list_of_products[product] += qty

print("Products in stock:")
[print(f"- {key}: {value}") for (key, value) in list_of_products.items()]
print(f"Total Products: {len(list_of_products)}")
print(f"Total Quantity: {sum(list_of_products.values())}")
