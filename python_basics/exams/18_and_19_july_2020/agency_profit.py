name = input()
number_tickets_adults = int(input())
number_tickets_kids = int(input())
price_per_ticket_adult = float(input())
service_fee = float(input())

price_per_ticket_kids = price_per_ticket_adult * 0.3
total_price = (number_tickets_adults * (price_per_ticket_adult + service_fee)) + (number_tickets_kids * (price_per_ticket_kids + service_fee))
profit = total_price * 0.2
print(f"The profit of your agency from {name} tickets is {profit:.2f} lv.")