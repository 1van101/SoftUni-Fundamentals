import math

magnolias_num = int(input())
zumbuls_num = int(input())
roses_num = int(input())
cactuses_num = int(input())
gift_price = float(input())

purchase_sum =(magnolias_num * 3.25 + zumbuls_num * 4 + roses_num * 3.50 + cactuses_num * 8) * 0.95
difference = abs(purchase_sum - gift_price)

if purchase_sum >= gift_price:
    print(f'She is left with {math.floor(difference)} leva.')
else:
    print(f"She will have to borrow {math.ceil(difference)} leva.")