number_of_loads = int(input())

price = 0
loads_by_bus = 0
loads_by_truck = 0
loads_by_train = 0

for loads in range(number_of_loads):
    weight_of_load = int(input())
    if weight_of_load <= 3:
        loads_by_bus += weight_of_load
        price += 200 * weight_of_load
    elif weight_of_load <= 11:
        loads_by_truck += weight_of_load
        price += 175 * weight_of_load
    else:
        loads_by_train += weight_of_load
        price += 120 * weight_of_load

weight_total = loads_by_bus + loads_by_train + loads_by_truck
average_price = price / weight_total
print(f"{average_price:.2f}")
print(f"{loads_by_bus/weight_total * 100:.2f}%")
print(f"{loads_by_truck/weight_total * 100:.2f}%")
print(f"{loads_by_train/weight_total * 100:.2f}%")