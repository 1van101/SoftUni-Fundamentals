resoursec_with_qty = {}

while True:
    key = input()
    if key == "stop":
        break
    value = int(input())

    if key not in resoursec_with_qty:
        resoursec_with_qty[key] = 0
    resoursec_with_qty[key] += value

for k, v in resoursec_with_qty.items():
    print(f"{k} -> {v}")