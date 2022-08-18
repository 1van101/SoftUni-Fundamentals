duration = input()
type_contract = input()
internet_added = input()
months = int(input())
price = 0
if duration == "one":
    if type_contract == "Small":
        price = 9.98
    elif type_contract == 'Middle':
        price = 18.99
    elif type_contract == 'Large':
        price = 25.98
    else:
        price = 35.99
else:
    if type_contract == "Small":
        price = 8.58
    elif type_contract == 'Middle':
        price = 17.09
    elif type_contract == 'Large':
        price = 23.59
    else:
        price = 31.79
if internet_added == "yes":
    if price <= 10:
        price += 5.5
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85
if duration == "two":
    price *= 0.9625
total_price = price * months
print(f"{total_price:.2f} lv.")




