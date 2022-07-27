def take_characters_on_odd_indices(psswrd):
    new_password = [y for x, y in enumerate(psswrd) if x % 2 != 0]
    print("".join(new_password))
    return "".join(new_password)


def cut_a_substring(psswrd, i, length):
    substring = psswrd[i:i + length]
    new_psswrd = psswrd.replace(substring, "", 1)
    print(new_psswrd)
    return new_psswrd


def substitute(psswrd, substr, subst):
    if substr in psswrd:
        psswrd = psswrd.replace(substr, subst)
        print(psswrd)
    else:
        print("Nothing to replace!")
    return psswrd


password = input()
command = input()
while not command == "Done":
    tokens = command.split()
    action = tokens[0]
    if action == "TakeOdd":
        password = take_characters_on_odd_indices(password)
    elif action == "Cut":
        password = cut_a_substring(password, int(tokens[1]), int(tokens[2]))
    elif action == "Substitute":
        password = substitute(password, tokens[1], tokens[2])

    command = input()

print(f"Your password is: {password}")
