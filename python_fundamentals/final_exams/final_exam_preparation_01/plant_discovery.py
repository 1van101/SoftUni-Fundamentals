def rate_the_plant(dct, name, rating):
    if name in dct:
        dct[name]['ratings'].append(int(rating))
    else:
        print("error")
    return dct


def update_the_rarity(dct, name, new_rarity):
    if name in dct:
        dct[name]['rarity'] = new_rarity
    else:
        print("error")
    return dct


def remove_the_ratings(dct, name):
    if name in dct:
        dct[name]['ratings'] = []
    else:
        print("error")
    return dct

number_of_plants = int(input())
plants_dct = {}

for i in range(number_of_plants):
    name, rarity = input().split("<->")
    plants_dct[name]= {'rarity': 0, 'ratings': []}
    plants_dct[name]['rarity'] = int(rarity)

command = input()
while not command == "Exhibition":
    command = command.split(": ")
    if command[0] == "Rate":
        name, rating = command[1].split(" - ")
        plants_dct = rate_the_plant(plants_dct, name, int(rating))
    elif command[0] == "Update":
        name, new_rarity = command[1].split(" - ")
        plants_dct = update_the_rarity(plants_dct, name, int(new_rarity))
    elif command[0] == "Reset":
        remove_the_ratings(plants_dct, command[1])
    command = input()

print("Plants for the exhibition:")
for name in plants_dct.keys():
    if plants_dct[name]['ratings']:
        average_rating = sum(plants_dct[name]['ratings']) / len(plants_dct[name]['ratings'])
        print(f"- {name}; Rarity: {plants_dct[name]['rarity']}; Rating: {average_rating:.2f}")
    else:
        print(f"- {name}; Rarity: {plants_dct[name]['rarity']}; Rating: {len(plants_dct[name]['ratings']):.2f}")