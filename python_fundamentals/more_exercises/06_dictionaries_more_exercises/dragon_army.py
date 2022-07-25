dragons_dct = {}

number_of_dragons = int(input())
for _ in range(number_of_dragons):
    color, type, damage, health, armor = input().split()
    if not damage.isdigit():
        damage = 45
    if not health.isdigit():
        health = 250
    if not armor.isdigit():
        armor = 10
    if color not in dragons_dct:
        dragons_dct[color] = {type: {"dmg": int(damage), "health": int(health), "armor": int(armor)}}
    else:
        dragons_dct[color][type] = {"dmg": int(damage), "health": int(health), "armor": int(armor)}

for dragon_color, data in dragons_dct.items():
    sum_dmg = 0
    sum_health = 0
    sum_armor = 0
    data_sorted = dict(sorted(data.items(), key=lambda kv: kv[0]))
    for dragon_type, stats in data_sorted.items():
        sum_dmg += data[dragon_type]["dmg"]
        sum_health += data[dragon_type]["health"]
        sum_armor += data[dragon_type]["armor"]
    print(
        f"{dragon_color}::({sum_dmg / len(dragons_dct[dragon_color]):.2f}/"
        f"{sum_health / len(dragons_dct[dragon_color]):.2f}/"
        f"{sum_armor / len(dragons_dct[dragon_color]):.2f})")
    [print(f"-{x} -> damage: {y['dmg']}, health: {y['health']}, armor: {y['armor']}") for x, y in data_sorted.items()]


