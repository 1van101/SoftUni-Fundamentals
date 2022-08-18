strawberry_price = float(input())
bananas_qty = float(input())
oranges_qty = float(input())
raspberry_qty = float(input())
strawberries_qty = float(input())
raspberry_price = strawberry_price / 2
oranges_price = raspberry_price * 0.6
bananas_price = raspberry_price * 0.2
total_price = strawberry_price * strawberries_qty + raspberry_qty * raspberry_price + oranges_qty * oranges_price + bananas_price * bananas_qty
print(f"{total_price:.2f}")
