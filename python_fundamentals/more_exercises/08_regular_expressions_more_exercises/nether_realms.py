import re

text = input().strip()
text = text.split(",")
# text = re.split(", *", input())
demons = {}

for demon in text:
    demon = demon.strip()
    health = 0
    damage = 0
    demons[demon] = []
    health_matches = re.findall(r"([^0-9+\-*/.])", demon)
    damage_matches = re.finditer(r"(?:\+|-)?[0-9]+(?:\.[0-9]+)?", demon)
    multiplication_or_division = re.findall(r"[*/]", demon)
    for char in health_matches:
        health += ord(char)

    for match in damage_matches:
        damage += float(match.group(0))
    for symbol in multiplication_or_division:
        if symbol == "*":
            damage *= 2
        elif symbol == "/":
            damage /= 2

    demons[demon].append(health)
    demons[demon].append(damage)

for d, qtys in sorted(demons.items()):
    print(f"{d} - {qtys[0]} health, {qtys[1]:.2f} damage")



