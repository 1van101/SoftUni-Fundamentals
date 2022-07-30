days_for_stay = int(input())
type_of_room = input()
rating = input()

price = 0
nights = days_for_stay - 1

if type_of_room == "room for one person":
    price = 18.00
elif type_of_room == "apartment":
    price = 25.00
    if nights < 10:
        price *= 0.7
    elif 10 <= nights <= 15:
        price *= 0.65
    else:
        price *= 0.5
elif type_of_room == "president apartment":
    price = 35.00
    if nights < 10:
        price *= 0.9
    elif 10 <= nights <= 15:
        price *= 0.85
    else:
        price *= 0.80
if rating == "positive":
    price *= 1.25
elif rating == "negative":
    price *= 0.9

total_price_discounted = nights * price
print (f"{total_price_discounted:.2f}")