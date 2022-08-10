budget = float(input())
category = input()
number_of_people = int(input())

transport_price = 0
ticket_price = 0

if 1 <= number_of_people <= 4:
    transport_price = budget * 0.75
elif 5 <= number_of_people <= 9:
    transport_price = budget * 0.6
elif 10 <= number_of_people <= 24:
    transport_price = budget * 0.5
elif 25 <= number_of_people <= 49:
    transport_price = budget * 0.4
else:
    transport_price = budget * 0.25

if category == "VIP":
    ticket_price = 499.99
elif category == "Normal":
    ticket_price = 249.99

total_costs = transport_price + ticket_price * number_of_people
difference = abs(budget - total_costs)

if budget >= total_costs:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
