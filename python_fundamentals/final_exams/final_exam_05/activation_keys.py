def contain_substring(key, sub):
    if sub in key:
        print(f"{key} contains {sub}")
    else:
        print("Substring not found!")


def make_letters_upper(key, start, end):
    sub = ""
    for ch in key[start:end]:
        sub += ch.upper()
    key = key[:start] + "".join(sub) + key[end:]
    print(key)
    return key


def make_letters_lower(key, start, end):
    sub = ""
    for ch in key[start:end]:
        sub += ch.lower()
    key = key[:start] + "".join(sub) + key[end:]
    print(key)
    return key


def delete_chars_between_indices(key, start, end):
    key = key[:start] + key[end:]
    print(key)
    return key


activation_key = input()
command = input()
while not command == "Generate":
    command = command.split(">>>")
    action = command[0]
    if action == "Contains":
        contain_substring(activation_key, command[1])
    elif action == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])
        if command[1] == "Upper":
            activation_key = make_letters_upper(activation_key, start_index, end_index)
        else:
            activation_key = make_letters_lower(activation_key, start_index, end_index)
    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = delete_chars_between_indices(activation_key, start_index, end_index)

    command = input()

print(f"Your activation key is: {activation_key}")
