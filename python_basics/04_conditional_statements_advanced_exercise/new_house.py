type_flower = input()
number_of_flowers = int(input())
budget = int(input())

price = 0

if type_flower == "Roses":
    price = 5
    if number_of_flowers > 80:
        price *= 0.9
elif type_flower == "Dahlias":
    price = 3.80
    if number_of_flowers > 90:
        price *= 0.85
elif type_flower == "Tulips":
    price = 2.80
    if number_of_flowers > 80:
        price *= 0.85
elif type_flower == "Narcissus":
    price = 3
    if number_of_flowers < 120:
        price *= 1.15
elif type_flower == "Gladiolus":
    price = 2.50
    if number_of_flowers < 80:
        price *= 1.2

total_price = number_of_flowers * price
difference = abs(budget - total_price)

if total_price <= budget:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
