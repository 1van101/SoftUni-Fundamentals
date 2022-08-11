heritage = float(input())
year_final = int(input())

total_spends = 0
age = 18

for year in range(1800, year_final + 1 ):
    if year % 2 == 0:
        total_spends += 12000
    else:
        total_spends += 12000 + 50 * age
    age += 1
difference = abs(heritage - total_spends)
if heritage >= total_spends:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
else:
    print(f"He will need {difference:.2f} dollars to survive.")