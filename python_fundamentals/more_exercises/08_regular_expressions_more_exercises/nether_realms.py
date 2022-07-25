import re


def altering_dmg(operators, dmg):
    for operator in operators:
        if operator == "*":
            dmg *= 2
        else:
            dmg /= 2
    return dmg


demons = re.split(r"\s*,\s*", input())
demons_dct = {}

for demon in demons:
    operators = re.findall(r"[*/]", demon)
    current_demon_health = sum(ord(x) for x in re.findall(r"[^\d\-+*/.]", demon))
    current_demon_dmg = sum([float(x.group(0)) for x in re.finditer(r"-*\d+(\.\d+)*", demon)])

    if operators:
        current_demon_dmg = altering_dmg(operators, current_demon_dmg)
    demons_dct[demon] = {"health": current_demon_health, "dmg": current_demon_dmg}

for current_demon in sorted(demons_dct.keys()):
    print(
        f"{current_demon} - {demons_dct[current_demon]['health']} health, {demons_dct[current_demon]['dmg']:.2f} damage")
