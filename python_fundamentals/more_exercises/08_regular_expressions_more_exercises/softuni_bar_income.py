import re

total_income = 0
while True:
    command = input()
    if command == "end of shift":
        break
    matches = re.finditer(r"^%([A-Z][a-z]+)%[^|$%.]*<([^>]+)>([^|$%.]+)?\|(\3)?([0-9]+)(\3)?\|([^|$%.0-9]+)?(\d+(\.\d+)?)\$$", command)
    for match in matches:
        name = match.group(1)
        product = match.group(2)
        price = float(match.group(8))
        qty = int(match.group(5))
        total_price = qty * price
        total_income += total_price
        print(f"{name}: {product} - {total_price:.2f}")

print(f"Total income: {total_income:.2f}")