to_do_list = [""] * 11

while True:
    command = input()
    if command == "End":
        break
    command_as_list = command.split("-")
    importance_num = int(command_as_list[0])
    activity = command_as_list[1]
    to_do_list.pop(importance_num)
    to_do_list.insert(importance_num, activity)


sorted_to_do_list = [x for x in to_do_list if x != ""]
print(sorted_to_do_list)

