flour_price = float(input())
flour_qty = float(input())
sugar_qty = float(input())
eggshell_num = int(input())
yeast = int(input())
sugar_price = flour_price * 0.75
eggshell_price = flour_price * 1.1
yeast_price = sugar_price * 0.2
total_price = flour_price * flour_qty + sugar_price * sugar_qty + eggshell_price * eggshell_num + yeast * yeast_price
print(f"{total_price:.2f}")