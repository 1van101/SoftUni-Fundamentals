city = input()
sales_volume = float(input())

comission = 0
is_valid = True

if city == "Sofia":
    if 0 <= sales_volume <= 500:
        comission = 0.05
    elif 500 < sales_volume <=1000:
        comission = 0.07
    elif 1000 < sales_volume <= 10000:
        comission = 0.08
    elif sales_volume > 10000:
        comission = 0.12
    else:
        is_valid = False
elif city == "Varna":
    if 0 <= sales_volume <= 500:
        comission = 0.045
    elif 500 < sales_volume <=1000:
        comission = 0.075
    elif 1000 < sales_volume <= 10000:
        comission = 0.1
    elif sales_volume > 10000:
        comission = 0.13
    else:
        is_valid = False
elif city == "Plovdiv":
    if 0 <= sales_volume <= 500:
        comission = 0.055
    elif 500 < sales_volume <=1000:
        comission = 0.08
    elif 1000 < sales_volume <= 10000:
        comission = 0.12
    elif sales_volume > 10000:
        comission = 0.145
    else:
        is_valid = False
else:
    is_valid = False

comission_total = comission * sales_volume
if is_valid:
    print(f"{comission_total:.2f}")
else:
    print("error")