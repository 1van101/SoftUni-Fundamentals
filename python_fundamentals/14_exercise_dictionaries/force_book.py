def word_in_values(dct, word):
    for words in dct.values():
        if word in words:
            return True
    return False


def remove_word_from_values(dct, word):
    for words in dct.values():
        if word in words:
            words.remove(word)
    return dct


def create_or_add_user(dct, side, user):
    if side not in dct:
        dct[side] = []
    if not word_in_values(dct, user):
        dct[side].append(user)
    return dct


def change_side_of_user(dct, user, side):
    if side not in dct:
        dct[side] = []
    if word_in_values(dct, user):
        remove_word_from_values(dct, user)
    dct[side].append(user)
    print(f"{force_user} joins the {force_side} side!")
    return dct


users = {}

command = input()
while not command == "Lumpawaroo":
    if " | " in command:
        force_side, force_user = command.split(" | ")
        users = create_or_add_user(users, force_side, force_user)
    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        users = change_side_of_user(users, force_user, force_side)
    command = input()

for k, v in users.items():
    if v:
        print(f"Side: {k}, Members: {len(v)}")
        [print(f"! {x}") for x in v]