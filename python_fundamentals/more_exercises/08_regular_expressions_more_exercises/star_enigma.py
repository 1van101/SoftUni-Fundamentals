import re


def decrypting_message(text):
    count_of_letters = len(re.findall(r"[star]", text, re.I))
    decrypted_message = ''.join(chr(ord(x) - count_of_letters) for x in text)
    return decrypted_message


def add_planets(text):
    matches = re.finditer(r"@(?P<planet>[A-Za-z]+)[^A\-!:>]*:(\d+)[^A\-!:>]*!(?P<attack_type>[AD]{1})![^A\-!:>]*->(\d+)", text)
    for match in matches:
        planets[match.group("attack_type")].append(match.group("planet"))


def print_data(planets, attack_type):
    if planets[attack_type]:
        [print(f"-> {x}") for x in sorted(planets[attack_type])]


lines = int(input())
planets = {'A': [], 'D': []}

for i in range(lines):
    text = input()
    decrypted_message = decrypting_message(text)
    add_planets(decrypted_message)

print(f"Attacked planets: {len(planets['A'])}")
print_data(planets, 'A')
print(f"Destroyed planets: {len(planets['D'])}")
print_data(planets, 'D')
