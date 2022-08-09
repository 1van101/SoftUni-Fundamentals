kilometers = int(input())
day_or_night = input()
price_by_taxi = 0
if day_or_night == "day":
    price_by_taxi = kilometers * 0.79 + 0.7
else:
    price_by_taxi = kilometers * 0.90 + 0.7

price_by_bus = kilometers * 0.09
price_by_train = kilometers * 0.06

if kilometers >= 100:
    print(f"{price_by_train:.2f}")
elif kilometers >=20:
    print(f"{price_by_bus:.2f}")
else:
    print(f"{price_by_taxi:.2f}")


