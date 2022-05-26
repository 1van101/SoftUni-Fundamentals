import re

total_money_spend = 0
furnitures = []
while True:
    command = input()
    if command == "Purchase":
        break

    matches = re.finditer(r"^>>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)$", command)
    for match in matches:
        price = float(match.group(2))
        quantity = int(match.group(4))
        total_money_spend += price * quantity
        furnitures.append(match.group(1))

print("Bought furniture:")
[print(x) for x in furnitures]
print(f"Total money spend: {total_money_spend:.2f}")
