progress_of_tournament = input()
ticket_type = input()
number_of_tickets = int(input())
photo_with_trophy = input()
price = 0
free_photos = False
if ticket_type == "Standard":
    if progress_of_tournament == "Quarter final":
        price = 55.50
    elif progress_of_tournament == "Semi final":
        price = 75.88
    elif progress_of_tournament == "Final":
        price = 110.10
elif ticket_type == "Premium":
    if progress_of_tournament == "Quarter final":
        price = 105.20
    elif progress_of_tournament == "Semi final":
        price = 125.22
    elif progress_of_tournament == "Final":
        price = 160.66
elif ticket_type == "VIP":
    if progress_of_tournament == "Quarter final":
        price = 118.90
    elif progress_of_tournament == "Semi final":
        price = 300.40
    elif progress_of_tournament == "Final":
        price = 400
total_price = price * number_of_tickets
if total_price > 4000:
    free_photos = True
if free_photos:
    total_price = total_price * 0.75
else:
    if total_price > 2500:
        total_price *= 0.9
    else:
        total_price = total_price
    if photo_with_trophy == "Y":
        total_price = total_price + number_of_tickets * 40

print(f"{total_price:.2f}")
