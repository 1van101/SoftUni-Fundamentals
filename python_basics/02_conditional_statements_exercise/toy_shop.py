trip_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

toys_sold = number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks
money_earn = (number_of_puzzles * 2.60 + number_of_dolls * 3 + number_of_bears * 4.10 + number_of_minions * 8.20 + number_of_trucks * 2) * 0.9
if toys_sold >= 50:
    money_earn = money_earn * 0.75
money_left = abs(money_earn - trip_price)

if trip_price <= money_earn:
    print (f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {money_left:.2f} lv needed.")