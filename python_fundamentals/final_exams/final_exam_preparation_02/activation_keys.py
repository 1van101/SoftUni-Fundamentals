def print_substring_availability(key, sub):
    if sub in key:
        print(f"{key} contains {sub}")
    else:
        print("Substring not found!")


def change_with_upper(key, start, end):
    substr_to_upper = (key[start:end]).upper()
    key = key[:start] + substr_to_upper + key[end:]
    print(key)
    return key


def change_with_lower(key, start, end):
    substr_to_lower = (key[start:end]).lower()
    key = key[:start] + substr_to_lower + key[end:]
    print(key)
    return key


def delete_some_chars(key, start, end):
    key = key[:start] + key[end:]
    print(key)
    return key


raw_activation_key = input()
command = input()
while not command == "Generate":
    command = command.split(">>>")
    action = command[0]
    if action == "Contains":
        print_substring_availability(raw_activation_key, command[1])
    elif action == "Flip":
        if command[1] == "Upper":
            raw_activation_key = change_with_upper(raw_activation_key, int(command[2]), int(command[3]))
        elif command[1] == "Lower":
            raw_activation_key = change_with_lower(raw_activation_key, int(command[2]), int(command[3]))
    elif action == "Slice":
        raw_activation_key = delete_some_chars(raw_activation_key, int(command[1]), int(command[2]))

    command = input()

print(f"Your activation key is: {raw_activation_key}")