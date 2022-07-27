def rate(dct, plant, rating):
    if plant not in dct:
        print("error")
    else:
        dct[plant]["ratings"].append(int(rating))
    return dct


def update(dct, plant, new_rarity):
    if plant not in dct:
        print("error")
    else:
        dct[plant]["rarity"] = new_rarity
    return dct


def reset(dct, plant):
    if plant not in dct:
        print("error")
    else:
        dct[plant]["ratings"] = []
    return dct


n = int(input())
plants_dct = {}

for i in range(n):
    plant, rarity = input().split("<->")
    plants_dct[plant] = {"rarity": int(rarity), "ratings":[]}

command = input()
while not command == "Exhibition":
    action, data = command.split(": ")

    if action == "Rate":
        plant, rating = data.split(" - ")
        plants_dct = rate(plants_dct, plant, int(rating))
    elif action == "Update":
        plant, new_rarity = data.split(" - ")
        plants_dct = update(plants_dct, plant, new_rarity)
    elif action == "Reset":
        plant = data
        plants_dct = reset(plants_dct, plant)

    command = input()
print("Plants for the exhibition:")
for k in plants_dct.keys():
    if plants_dct[k]["ratings"]:
        print(f"- {k}; Rarity: {plants_dct[k]['rarity']}; Rating: {sum(plants_dct[k]['ratings']) / len(plants_dct[k]['ratings']):.2f}")
    else:
        print(f"- {k}; Rarity: {plants_dct[k]['rarity']}; Rating: {len(plants_dct[k]['ratings']):.2f}")