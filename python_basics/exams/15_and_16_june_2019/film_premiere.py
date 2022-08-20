projection = input()
movie_package = input()
number_tickets = int(input())

price = 0

if projection == "John Wick":
    if movie_package == "Drink":
        price = 12
    elif movie_package =="Popcorn":
        price = 15
    elif movie_package == "Menu":
        price = 19
elif projection == "Star Wars":
    if movie_package == "Drink":
        price = 18
    elif movie_package == "Popcorn":
        price = 25
    elif movie_package == "Menu":
        price = 30
    if number_tickets >= 4:
        price *= 0.7
else:
    if movie_package == "Drink":
        price = 9
    elif movie_package == "Popcorn":
        price = 11
    elif movie_package == "Menu":
        price = 14
    if number_tickets == 2:
        price *= 0.85

total_price = price * number_tickets
print(f"Your bill is {total_price:.2f} leva.")

