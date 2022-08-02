def change_first_n_chars_back(message, num):
    return message[num:] + message[:num]


def insert_value(message, i, value):
    return message[:i] + value + message[i:]


def change_all_occurrences(message, substr, replacement):
    return message.replace(substr, replacement)


message = input()

while True:
    command = input().split("|")
    action = command[0]
    if action == "Decode":
        break
    elif action == "Move":
        message = change_first_n_chars_back(message, int(command[1]))
    elif action == "Insert":
        message = insert_value(message, int(command[1]), command[2])
    elif action == "ChangeAll":
        message = change_all_occurrences(message, command[1], command[2])

print(f"The decrypted message is: {message}")
