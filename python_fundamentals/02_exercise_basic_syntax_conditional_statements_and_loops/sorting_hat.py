everybody_are_sorted = False
while True:
    command = input()
    if command == "Welcome!":
        everybody_are_sorted = True
        break
    if command == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    else:
        print(f"{command} goes to Hufflepuff.")

if everybody_are_sorted:
    print("Welcome to Hogwarts.")