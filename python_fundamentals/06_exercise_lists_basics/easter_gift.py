gifts = input().split()

while True:

    command = input()
    if command == "No Money":
        break
    command = command.split()
    if "OutOfStock" in command:
        for word in gifts:
            if word == command[1]:
                gifts[gifts.index(word)] = "None"
    elif "Required" in command:
        if 0 < int(command[2]) < len(gifts):
            gifts[int(command[2])] = command[1]
    elif "JustInCase" in command:
        gifts[-1] = command[1]

while "None" in gifts:
    gifts.remove("None")

for gift in gifts:
    print(gift, end=" ")
