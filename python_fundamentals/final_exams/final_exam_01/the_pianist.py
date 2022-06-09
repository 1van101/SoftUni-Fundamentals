def add(data, collection):
    piece = data[1]
    composer = data[2]
    key = data[3]
    if piece in collection.keys():
        print(f"{piece} is already in the collection!")
    else:
        collection[piece] = {"Composer": composer, "Key": key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    return collection


def remove(data, collection):
    piece = data[1]
    if piece in collection.keys():
        print(f"Successfully removed {piece}!")
        del collection[piece]
        return collection
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return collection

def change_the_key(data, collection):
    piece = data[1]
    new_key = data[2]
    if piece in collection.keys():
        collection[piece]["Key"] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return collection



num_of_pieces = int(input())
composers_and_keys = {}

for line in range(num_of_pieces):
    piece, composer, key = input().split("|")
    composers_and_keys[piece] = {"Composer": composer, "Key": key}

command = input()
while command != "Stop":
    current_command = command.split("|")
    action = current_command[0]
    if action == "Add":
        composers_and_keys = add(current_command, composers_and_keys)
    elif action == "Remove":
        composers_and_keys = remove(current_command, composers_and_keys)
    elif action == "ChangeKey":
        composers_and_keys = change_the_key(current_command, composers_and_keys)

    command = input()

for piece, value in composers_and_keys.items():
    composer = value["Composer"]
    key = value["Key"]
    print(f"{piece} -> Composer: {composer}, Key: {key}")