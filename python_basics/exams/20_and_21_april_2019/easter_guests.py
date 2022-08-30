import math

guests_num = int(input())
budget = int(input())
easter_breads_num = math.ceil(guests_num / 3)
eggs_num = guests_num * 2
total_price = easter_breads_num * 4 + eggs_num * 0.45
diff = abs(budget - total_price)
if budget >= total_price:
    print(f"Lyubo bought {easter_breads_num} Easter bread and {eggs_num} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")