type_fuel = input()
volume_fuel = float(input())
club_card = input()

total_price = 0

if type_fuel == "Gasoline":
    if club_card == "Yes":
        total_price = volume_fuel * (2.22 - 0.18)
    else:
        total_price = volume_fuel * 2.22
elif type_fuel == "Diesel":
    if club_card == "Yes":
        total_price = volume_fuel * (2.33 - 0.12)
    else:
        total_price = volume_fuel * 2.33
if type_fuel == "Gas":
    if club_card == "Yes":
        total_price = volume_fuel * (0.93 - 0.08)
    else:
        total_price = volume_fuel * 0.93

if 20 <= volume_fuel <= 25:
    total_price *= 0.92
elif volume_fuel > 25:
    total_price *= 0.9

print (f"{total_price:.2f} lv.")
