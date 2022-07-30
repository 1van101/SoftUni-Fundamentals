month = input()
number_of_nights = int(input())

price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if number_of_nights > 14:
        price_studio *=0.70
    elif number_of_nights > 7:
        price_studio *=0.95
elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if number_of_nights > 14:
        price_studio *= 0.8
elif month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77
if number_of_nights > 14:
    price_apartment *= 0.9

total_price_apartment = number_of_nights * price_apartment
total_price_studio = number_of_nights * price_studio

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
