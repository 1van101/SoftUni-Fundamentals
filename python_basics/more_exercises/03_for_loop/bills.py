months = int(input())

electricity = 0
water = 0
internet = 0
others = 0

for m in range (1, months + 1):
    electricity_bill = float(input())
    water_bill = 20
    internet_bill = 15
    electricity += electricity_bill
    water += 20
    internet += 15
    others += (electricity_bill + water_bill + internet_bill) * 1.2

average = (electricity + water + internet + others) / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average:.2f} lv")
