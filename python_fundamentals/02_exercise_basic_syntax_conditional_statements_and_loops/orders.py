num_of_orders = int(input())
total_price = 0
for order in range(num_of_orders):

    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    if 0.01 <= price_per_capsule <=100 and 1 <= days <= 31 and 1 <= capsules_count <= 2000:
        current_price = price_per_capsule * days * capsules_count
        total_price += current_price
        print(f"The price for the coffee is: ${current_price:.2f}")
print(f"Total: ${total_price:.2f}")