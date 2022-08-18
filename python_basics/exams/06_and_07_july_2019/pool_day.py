import math

people_num = int(input())
tax = float(input())
price_per_chair = float(input())
price_per_umbrella = float(input())

people_with_chair = people_num * 0.75
people_with_umbrella = people_num / 2
total_price = (people_num * tax) + (math.ceil(people_with_chair) * price_per_chair) + (price_per_umbrella * math.ceil(people_with_umbrella))

print(f"{total_price:.2f} lv.")
