budget = float(input())
number_statists = int(input())
uniform_per_statists = float(input())

decor = budget * 0.1
if number_statists > 150:
    uniform_per_statists = uniform_per_statists * 0.9
sum_total = number_statists * uniform_per_statists + decor
difference = abs(sum_total - budget)
if sum_total > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
elif sum_total <= budget:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
