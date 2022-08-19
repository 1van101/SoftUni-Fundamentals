movie_name = input()
hall_type = input()
tickets_number = int(input())
price = 0

if hall_type == "normal":
    if movie_name == "A Star Is Born":
        price = 7.5
    elif movie_name == "Bohemian Rhapsody":
        price = 7.35
    elif movie_name == "Green Book":
        price = 8.15
    else:
        price = 8.75
elif hall_type == "luxury":
    if movie_name == "A Star Is Born":
        price = 10.50
    elif movie_name == "Bohemian Rhapsody":
        price = 9.45
    elif movie_name == "Green Book":
        price = 10.25
    else:
        price = 11.55
else:
    if movie_name == "A Star Is Born":
        price = 13.50
    elif movie_name == "Bohemian Rhapsody":
        price = 12.75
    elif movie_name == "Green Book":
        price = 13.25
    else:
        price = 13.95
total_price = price * tickets_number
print(f"{movie_name} -> {total_price:.2f} lv.")