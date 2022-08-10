season = input()
type_of_group = input()
number_of_students = int(input())
number_of_overnights = int(input())
price = 0
type_of_sport = ""
if season == "Winter":
    if type_of_group == "boys":
        price = 9.60
        type_of_sport = "Judo"
    elif type_of_group == "girls":
        price = 9.60
        type_of_sport = "Gymnastics"
    else:
        price = 10
        type_of_sport = "Ski"
if season == "Spring":
    if type_of_group == "boys":
        price = 7.20
        type_of_sport = "Tennis"
    elif type_of_group == "girls":
        price = 7.20
        type_of_sport = "Athletics"
    else:
        price = 9.50
        type_of_sport = "Cycling"
if season == "Summer":
    if type_of_group == "boys":
        type_of_sport = "Football"
        price = 15
    elif type_of_group == "girls":
        price = 15
        type_of_sport = "Volleyball"
    else:
        price = 20
        type_of_sport = "Swimming"

total_price = number_of_overnights * number_of_students * price

if 10 <= number_of_students < 20:
    total_price *= 0.95
elif 20 <= number_of_students < 50:
    total_price *= 0.85
elif number_of_students >= 50:
    total_price *= 0.5
else:
    total_price = total_price

print(f"{type_of_sport} {total_price:.2f} lv.")

