def get_chars_on_odd_indices(raw_password):
    raw_password = [y for x, y in enumerate(raw_password) if x % 2 != 0]
    print("".join(raw_password))
    return "".join(raw_password)


def cut_a_substring(raw_password, i, length):
    raw_password = raw_password[:i] + raw_password[i + length:]
    print(raw_password)
    return raw_password


def get_replaced_password(raw_password, substr, substitute):
    if substr in raw_password:
        raw_password = raw_password.replace(substr, substitute)
        print(raw_password)
    else:
        print("Nothing to replace!")
    return raw_password

password = input()

command = input()
while not command == "Done":
    command = command.split()
    action = command[0]
    if action == "TakeOdd":
        password = get_chars_on_odd_indices(password)
    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        password = cut_a_substring(password, index, length)
    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        password = get_replaced_password(password, substring, substitute)
    command = input()

print(f"Your password is: {password}")