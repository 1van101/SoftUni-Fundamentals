bags_price_more_than_20 = float(input())
weight_of_bags = float(input())
days = int(input())
number_bags = int(input())

total_price = 0

if weight_of_bags < 10:
    total_price = bags_price_more_than_20 * 0.2
elif weight_of_bags <= 20:
    total_price = bags_price_more_than_20 * 0.5
else:
    total_price = bags_price_more_than_20

if days < 7 :
    total_price *= 1.4
elif days <= 30:
    total_price *= 1.15
else:
    total_price *= 1.1

total_price *= number_bags

print(f"The total price of bags is: {total_price:.2f} lv. ")
