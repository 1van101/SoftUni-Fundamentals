def insert_space(mssg, i):
    mssg = mssg[:i] + " " + mssg[i:]
    print(mssg)
    return mssg


def reverse(mssg, substr):
    if substr in mssg:
        cutted_mssg = mssg.replace(substr, "", 1)
        mssg = cutted_mssg + substr[::-1]
        print(mssg)
        return mssg
    else:
        print("error")
    return mssg


def change_all(mssg, substr, replace):
    new_mssg = mssg.replace(substr, replace)
    print(new_mssg)
    return new_mssg


concealed_mssg = input()

instructions = input()
while instructions != "Reveal":
    tokens = instructions.split(":|:")
    action = tokens[0]
    if action == "InsertSpace":
        concealed_mssg = insert_space(concealed_mssg, int(tokens[1]))
    elif action == "Reverse":
        concealed_mssg = reverse(concealed_mssg, tokens[1])
    elif action == "ChangeAll":
        concealed_mssg = change_all(concealed_mssg, tokens[1], tokens[2])

    instructions = input()

print(f"You have a new text message: {concealed_mssg}")
