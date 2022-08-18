days = int(input())
hours_daily = int(input())
total_price = 0
for d in range(1, days + 1):
    day_counter = 0
    for h in range(1, hours_daily + 1):
        if d % 2 == 0 and h % 2 != 0:
            total_price += 2.50
            day_counter += 2.50
        elif d % 2 != 0 and h % 2 == 0:
            total_price += 1.25
            day_counter += 1.25
        else:
            total_price += 1
            day_counter += 1
    print(f"Day: {d} - {day_counter:.2f} leva")
print(f"Total: {total_price:.2f} leva")

