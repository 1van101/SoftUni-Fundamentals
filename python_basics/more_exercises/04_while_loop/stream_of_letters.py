secret_word = ""
letters = ""
c_counter = 0
o_counter = 0
n_counter = 0

while True:
    command = input()
    if command == "End":
        break
    if command == "c" and c_counter < 1:
        c_counter += 1

    elif command == "o" and o_counter < 1:
        o_counter += 1
    elif command == "n" and n_counter < 1:
        n_counter += 1
    else:
        if command.isalpha():
            letters += command
    if c_counter and o_counter and n_counter == 1:
        secret_word += letters
        secret_word += " "
        letters = ""
        c_counter = 0
        o_counter = 0
        n_counter = 0

print(secret_word)