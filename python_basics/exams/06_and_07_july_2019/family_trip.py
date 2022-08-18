budget = float(input())
number_nights = int(input())
price_per_night = float(input())
additional_costs_percent = int(input())

total_costs = number_nights * price_per_night
additional_costs = budget * additional_costs_percent / 100

if number_nights > 7:
     total_costs *= 0.95

total_costs_total = total_costs + additional_costs
diff = abs(budget - total_costs_total)

if budget >= total_costs_total:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")