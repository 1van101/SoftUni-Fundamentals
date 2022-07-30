budget = int(input())
season = input()
qty_fishermans = int(input())
price = 0
if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600


if qty_fishermans <= 6:
    price *= 0.9
elif 7 < qty_fishermans <= 11:
    price *= 0.85
else:
    price *= 0.75

if qty_fishermans % 2 == 0 and season != "Autumn":
    price *= 0.95

diff = abs(budget - price)
if budget >= price:
    print (f"Yes! You have {diff:.2f} leva left.")
else:
    print (f"Not enough money! You need {diff:.2f} leva.")