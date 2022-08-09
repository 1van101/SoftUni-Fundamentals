import math

vineyard_area = int(input())
grapes_per_square_meter = float(input())
wine_needed_in_litres = int(input())
workers = int(input())

grapes_for_wine_area = vineyard_area * 0.4
produced_wine = grapes_for_wine_area * grapes_per_square_meter / 2.5

difference = abs(wine_needed_in_litres - produced_wine)
wine_for_one_worker = difference / workers

if produced_wine < wine_needed_in_litres:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(produced_wine)} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(wine_for_one_worker)} liters per person.")