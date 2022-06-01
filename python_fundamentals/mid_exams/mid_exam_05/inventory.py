def collect_item(it_list, it):
    if it not in it_list:
        it_list.append(it)
    return it_list


def drop_item(it_list, it):
    if it in it_list:
        it_list.remove(it)
    return it_list


def combine_items(it_list, old_it, new_it):
    if old_it in it_list:
        index_old_it = it_list.index(old_it)
        it_list.insert(index_old_it + 1, new_it)
    return it_list


def renew_list(it_list, it):
    if it in it_list:
        index_it = it_list.index(it)
        popped_item = it_list.pop(index_it)
        it_list.append(popped_item)
    return it_list


collecting_items = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break

    command = command.split(" - ")
    item = command[1]

    if "Collect" in command:
        collecting_items = collect_item(collecting_items, item)
    elif "Drop" in command:
        collecting_items = drop_item(collecting_items, item)
    elif "Combine Items" in command:
        item = item.split(":")
        old_item = item[0]
        new_item = item[1]
        collecting_items = combine_items(collecting_items, old_item, new_item)
    elif "Renew" in command:
        collecting_items = renew_list(collecting_items, item)

print(", ".join(collecting_items))
