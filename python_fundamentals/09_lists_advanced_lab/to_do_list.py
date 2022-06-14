def add_note_to_list(to_do_list, i, act):
    to_do_list.pop(i)
    to_do_list.insert(i, act)
    return to_do_list


to_do_list = [""] * 11
while True:
    command = input()
    if command == "End":
        break
    importance_i, action = command.split("-")
    to_do_list = add_note_to_list(to_do_list, int(importance_i), action)

to_do_list = [x for x in to_do_list if x != ""]
print(to_do_list)