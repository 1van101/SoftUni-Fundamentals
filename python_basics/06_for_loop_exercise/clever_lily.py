lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

birthday_money = 0
birthday_toys = 0
savings = 0

for current_age in range (1, lily_age + 1):
    if current_age % 2 == 0:
        birthday_money += 10 * current_age // 2
        birthday_money -= 1
    else:
        birthday_toys += 1

savings = birthday_money + birthday_toys * toy_price
difference = abs(savings - washing_machine_price)

if savings >= washing_machine_price:
    print (f'Yes! {difference:.2f}')
else:
    print(f"No! {difference:.2f}")
