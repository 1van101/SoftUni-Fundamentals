def get_loot(treasure, items):
    for index in range(1, len(items)):
        if items[index] not in treasure:
            treasure.insert(0, items[index])
    return treasure


def drop_loot(treasure, index):
    if index < len(treasure):
        popped_item = treasure.pop(index)
        treasure.append(popped_item)
    return treasure


def steal(treasure, count):
    if count >= len(treasure):
        print(", ".join(treasure))
        treasure.clear()
        return treasure

    start_index_for_stolen_items = len(treasure) - count
    end_index_for_new_treasure = start_index_for_stolen_items
    stolen_items = treasure[start_index_for_stolen_items:]
    print(", ".join(stolen_items))
    return treasure[:end_index_for_new_treasure]


def get_avg_treasure_gain(treasure):
    sum_of_chars = 0
    if len(treasure) > 0:
        for item in treasure:
            sum_of_chars += len(item)
        treasure_gain = sum_of_chars / len(treasure)
        return treasure_gain


def print_treasure(treasure, avg_gain):
    if len(treasure) == 0:
        print("Failed treasure hunt.")
    else:
        print(f"Average treasure gain: {avg_gain:.2f} pirate credits.")


treasure_chest = input().split("|")

while True:
    command = input()
    if command == "Yohoho!":
        break

    command = command.split()
    action = command[0]
    if action == "Loot":
        treasure_chest = get_loot(treasure_chest, command)
    elif action == "Drop":
        treasure_chest = drop_loot(treasure_chest, int(command[1]))
    elif action == "Steal":
        treasure_chest = steal(treasure_chest, int(command[1]))

average_gain = get_avg_treasure_gain(treasure_chest)
print_treasure(treasure_chest, average_gain)
