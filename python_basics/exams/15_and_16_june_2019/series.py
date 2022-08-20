budget = float(input())
number_series = int(input())
total_price = 0
for i in range(number_series):
    name_series = input()
    price = float(input())
    if name_series == "Thrones":
        total_price += price * 0.5
    elif name_series == "Lucifer":
        total_price += price * 0.6
    elif name_series == "Protector":
        total_price += price * 0.7
    elif name_series == "TotalDrama":
        total_price += price * 0.8
    elif name_series == "Area":
        total_price += price * 0.9
    else:
        total_price += price
diff = abs(total_price - budget)
if budget >= total_price:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")