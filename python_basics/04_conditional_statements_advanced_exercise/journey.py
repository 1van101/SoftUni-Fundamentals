budget = float(input())
season = input()
price = 0
destination = ""
accomodation = ""
if budget <= 100:
    destination = "Bulgaria"
    if season =="summer":
        accomodation = "Camp"
        price = budget * 0.3
    elif season =="winter":
        accomodation = "Hotel"
        price = budget * 0.7
elif 100 < budget <=1000:
    destination = "Balkans"
    if season =="summer":
        accomodation = "Camp"
        price = budget * 0.4
    elif season =="winter":
        accomodation = "Hotel"
        price = budget * 0.8
# if budget > 1000:
else:
    destination = "Europe"
    price = budget * 0.9
    accomodation = "Hotel"
print (f"Somewhere in {destination}")
print (f"{accomodation} - {price:.2f}")