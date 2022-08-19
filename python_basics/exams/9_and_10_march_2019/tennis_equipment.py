import math

racket_price = float(input())
rackets_number = int(input())
shoes_number = int(input())
shoes_price = racket_price / 6
shoes_and_rackets_price = rackets_number * racket_price + shoes_price * shoes_number
other_equipment = shoes_and_rackets_price * 0.2
all_equipment = shoes_and_rackets_price + other_equipment
print(f"Price to be paid by Djokovic {math.floor(all_equipment / 8)}")
print(f"Price to be paid by sponsors {math.ceil(all_equipment * 7 / 8)}")