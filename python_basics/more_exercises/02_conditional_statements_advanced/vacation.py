budget = float(input())
season = input()
type_accommodation = ""
destination = ""
price = 0

if budget <= 1000:
    type_accommodation = "Camp"
    if season == "Summer":
        destination = "Alaska"
        price = budget * 0.65
    else:
        destination = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    type_accommodation = "Hut"
    if season == "Summer":
        destination = "Alaska"
        price = budget * 0.80
    else:
        destination = "Morocco"
        price = budget * 0.60
else:
    type_accommodation = "Hotel"
    if season == "Summer":
        destination = "Alaska"
        price = budget * 0.90
    else:
        destination = "Morocco"
        price = budget * 0.90

print(f"{destination} - {type_accommodation} - {price:.2f}")