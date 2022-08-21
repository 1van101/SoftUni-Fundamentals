qty = int(input())
joinery_size = input()
delivery = input()

is_invalid = False
price = 0
price_total = 0

if qty < 10:
    is_invalid = True
else:
    if joinery_size == "90X130":
        price = 110
        if 30 < qty <= 60:
            price *= 0.95
        elif qty > 60:
            price *= 0.92
    elif joinery_size == "100X150":
        price = 140
        if 40 < qty <= 80:
            price *= 0.94
        elif qty > 80:
            price *= 0.90
    elif joinery_size == "130X180":
        price = 190
        if 20 < qty <= 50:
            price *= 0.93
        elif qty > 50:
            price *= 0.88
    elif joinery_size == "200X300":
        price = 250
        if 25 < qty <= 50:
            price *= 0.91
        elif qty > 50:
            price *= 0.86

    if delivery == "With delivery":
        price_total = price * qty + 60
    else:
        price_total = price * qty
    if qty > 99:
        price_total *= 0.96

if is_invalid:
    print("Invalid order")
else:
    print(f"{price_total:.2f} BGN")







