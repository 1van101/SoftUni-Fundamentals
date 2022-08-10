cyclists_juniors = int(input())
cyclists_seniors = int(input())
race_type = input()
race_price_juniors = 0
race_price_seniors = 0
cyclists_total = cyclists_seniors + cyclists_juniors

if race_type == "trail":
    race_price_juniors = 5.50
    race_price_seniors = 7
elif race_type == "cross-country":
    race_price_juniors = 8
    race_price_seniors = 9.50
    if cyclists_total >= 50:
        race_price_juniors = 8 * 0.75
        race_price_seniors = 9.50 * 0.75
elif race_type == "downhill":
    race_price_juniors = 12.25
    race_price_seniors = 13.75
elif race_type == "road":
    race_price_juniors = 20
    race_price_seniors = 21.50

price_total = (cyclists_juniors * race_price_juniors + cyclists_seniors * race_price_seniors) * 0.95
print(f"{price_total:.2f}")
