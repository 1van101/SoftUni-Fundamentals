import re

lines = int(input())
letters = ["s", "t", "a", "r", "S", "T", "A", "R"]

planets = {"A": [], "D": []}
current_message_decrypted = []

for messages in range(lines):
    number_of_letters = 0
    current_message = input()
    for char in current_message:
        if char in letters:
            number_of_letters += 1

    current_message_decrypted = [chr(ord(x) - number_of_letters) for x in current_message]
    current_message_decrypted = "".join(current_message_decrypted)
    matches = re.finditer(r"@([A-Z][a-z]+)([^@\-!:>]*):(\d+)([^@\-!:>]*)!([AD])!([^@\-!:>]*)->([0-9]+)", current_message_decrypted)

    for match in matches:
        planet = match.group(1)
        type_of_attack = match.group(5)

        if planet not in planets[type_of_attack]:
            planets[type_of_attack].append(planet)


planets_sorted = {x:sorted(planets[x]) for x in planets.keys()}

for k, v in planets_sorted.items():
    if k == "A":
        print(f"Attacked planets: {len(planets_sorted[k])}")
        if len(planets_sorted[k]) > 0:
            for elements in v:
                print(f"-> {elements}")
    else:
        print(f"Destroyed planets: {len(planets_sorted[k])}")
        if len(planets_sorted[k]) > 0:
            for elements in v:
                print(f"-> {elements}")
