name = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
percent_for_cinema = int(input())

profit = days * tickets * ticket_price
total_profit = profit - (profit * percent_for_cinema / 100)
print(f"The profit from the movie {name} is {total_profit:.2f} lv.")