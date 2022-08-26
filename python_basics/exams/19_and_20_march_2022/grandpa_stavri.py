days = int(input())
litres_counter = 0
degrees_counter = 0

for day in range(days):
    amount_of_rakia = float(input())
    gradus_of_rakia = float(input())
    litres_counter += amount_of_rakia
    degrees_counter += gradus_of_rakia * amount_of_rakia

gradus_of_rakia_final = degrees_counter / litres_counter

print(f"Liter: {litres_counter:.2f}")
print(f"Degrees: {gradus_of_rakia_final:.2f}")
if gradus_of_rakia_final < 38:
    print("Not good, you should baking!")
elif gradus_of_rakia_final <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")