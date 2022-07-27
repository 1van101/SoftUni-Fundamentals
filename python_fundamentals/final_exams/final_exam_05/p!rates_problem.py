def plunder_the_town(targets, town, people, gold):
    targets[town]["population"] -= people
    targets[town]["gold"] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if targets[town]["population"] == 0 or targets[town]["gold"] == 0:
        del targets[town]
        print(f"{town} has been wiped off the map!")
    return targets


def increase_gold(targets, town, gold):
    if gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        targets[town]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {targets[town]['gold']} gold.")
    return targets


targets = {}

while True:
    command = input().split("||")
    if command[0] == "Sail":
        break
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in targets:
        targets[city] = {"population": 0, "gold": 0}
    targets[city]["population"] += population
    targets[city]["gold"] += gold

while True:
    event = input().split("=>")
    if event[0] == "End":
        break
    action = event[0]
    if action == "Plunder":
        town, num_people, gold = event[1], int(event[2]), int(event[3])
        targets = plunder_the_town(targets, town, num_people, gold)
    elif action == "Prosper":
        town, gold = event[1], int(event[2])
        targets = increase_gold(targets, town, gold)

if targets:
    print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
    [print(f"{x} -> Population: {y['population']} citizens, Gold: {y['gold']} kg") for x, y in targets.items()]
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
