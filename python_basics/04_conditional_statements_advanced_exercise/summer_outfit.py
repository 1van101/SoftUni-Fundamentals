temperature = int(input())
time_of_day = input()
Outfit = ""
Shoes = ""
if time_of_day == "Morning":
    if temperature >= 10 and temperature <= 18:
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif temperature > 18 and temperature <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif temperature >= 25:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
if time_of_day == "Afternoon":
    if temperature >= 10 and temperature <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif temperature > 18 and temperature <= 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif temperature >= 25:
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
if time_of_day == "Evening":
    if temperature >= 10 and temperature <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif temperature > 18 and temperature <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif temperature >= 25:
        Outfit = "Shirt"
        Shoes = "Moccasins"
print (f"It's {temperature} degrees, get your {Outfit} and {Shoes}.")





