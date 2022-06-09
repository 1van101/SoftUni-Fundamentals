import re

text = input()

list_of_products = []
nutriotion = 0
matches = re.finditer(r"(#|\|)(?P<item>[A-Za-z\s]+)\1(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<nutrition>[0-9]{1,5})\1", text)

for match in matches:
    list_of_products.append([match.group("item"), match.group("date"), match.group("nutrition")])
    nutriotion += int(match.group("nutrition"))

food_for_days = nutriotion // 2000
print(f"You have food to last you for: {food_for_days} days!")
for data in list_of_products:
    print(f"Item: {data[0]}, Best before: {data[1]}, Nutrition: {data[2]}")