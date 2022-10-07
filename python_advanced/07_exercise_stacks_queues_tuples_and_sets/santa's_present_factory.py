from collections import deque


def add_crafted_toys(current_toy):
    if current_toy == "Doll" or current_toy == "Wooden train":
        doll_and_train.add(current_toy)
    elif current_toy == "Teddy bear" or current_toy == "Bicycle":
        bear_and_bicycle.add(current_toy)


def positive_result(toys_dct, boxes, res, curr_box):
    for toy in toys_dct.keys():
        if toys_dct[toy]["magic"] == res:
            add_crafted_toys(toy)
            toys_dct[toy]["count"] += 1
            return toys_dct
    boxes.append(curr_box + 15)
    return toys_dct


def zero_result(curr_box, curr_magic):
    if curr_box != 0:
        materials.append(curr_box)
    if curr_magic != 0:
        magic.appendleft(curr_magic)


table = {
    "Doll": {'magic': 150, 'count': 0},
    "Wooden train": {'magic': 250, 'count': 0},
    "Teddy bear": {'magic': 300, 'count': 0},
    "Bicycle": {'magic': 400, 'count': 0}
}
doll_and_train = set()
bear_and_bicycle = set()

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

while materials and magic:
    current_box = materials.pop()
    current_magic = magic.popleft()
    res = current_box * current_magic

    if res < 0:
        materials.append(current_box + current_magic)
    elif res == 0:
        zero_result(current_box, current_magic)
    else:
        table = positive_result(table, materials, res, current_box)

presents_are_crafted = (len(doll_and_train) == 2) or (len(bear_and_bicycle) == 2)

if presents_are_crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(reversed([str(x) for x in materials]))}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")
[print(f"{x}: {table[x]['count']}") for x in sorted(table.keys()) if table[x]['count'] > 0]
