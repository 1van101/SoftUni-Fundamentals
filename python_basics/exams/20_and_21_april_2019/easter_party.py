guests_num = int(input())
price_per_person = float(input())
budget = float(input())

if 10 <= guests_num <= 15:
    price_per_person *= 0.85
elif 15 < guests_num <= 20:
    price_per_person *= 0.8
elif guests_num > 20:
    price_per_person *= 0.75
cake_price = budget * 0.1
total_price = guests_num * price_per_person + cake_price
diff = abs(budget - total_price)
if total_price <= budget:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")