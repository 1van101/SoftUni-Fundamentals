parking_lot = set()
num = int(input())

for _ in range(num):
    command, number = input().split(", ")
    if command == "IN":
        parking_lot.add(number)
    else:
        try:
            parking_lot.remove(number)
        except IndexError:
            continue

if parking_lot:
    print("\n".join(parking_lot))
else:
    print("Parking Lot is Empty")

