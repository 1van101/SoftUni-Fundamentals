def move(mssg, n_lttrs):
    if n_lttrs < len(mssg) and n_lttrs > 0:
        mssg = mssg[n_lttrs:] + mssg[:n_lttrs]
    return mssg


def insert(mssg, i, v):
    first_part_of_mssg = mssg[:i]
    second_part_of_mssg = mssg[i:]
    mssg = first_part_of_mssg + list(v) + second_part_of_mssg
    return mssg


def change_all(mssg, sub, rep):
    return [x if x != sub else rep for x in mssg]


message = list(input())
command = input()
while command != "Decode":
    data = command.split("|")
    action = data[0]
    if action == "Move":
        number_of_letters = int(data[1])
        message = move(message, number_of_letters)
    elif action == "Insert":
        index = int(data[1])
        value = data[2]
        message = insert(message, index, value)
    elif action == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        message = change_all(message, substring, replacement)

    command = input()
print(f"The decrypted message is: {''.join(message)}")