import re

text = input()
destinations = []
matches = re.finditer(r"(=|\/)(?P<destination>[A-Z][A-Za-z]{2,})\1", text)

for match in matches:
    destinations.append(match.group("destination"))

points = sum([len(x) for x in destinations])
print(f"Destinations: {', '.join(destinations)}\nTravel Points: {points}")
