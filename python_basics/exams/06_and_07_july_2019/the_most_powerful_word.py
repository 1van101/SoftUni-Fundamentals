

the_most_powerful_word = ""
points = 0
while True:
    command = input()
    current_points = 0
    if command == "End of words":
        break
    for symbol, char in enumerate(command):
        current_points += ord(char)

    for symbol, char in enumerate(command):
        if symbol == 0:
            # if char == "a" or char == "A" or char == "e" or char == "E"  or char == "i" or char == "I" or char == "o" or char == "O" or char =="u"\
            #     or char == "u"  or char == "U"  or char =="y" or char == "Y":
            if char in ("a","A","e","E","i","I","o","O","u","U","y","Y"):
                current_points *= len(command)
            else:
                current_points //= len(command)
        else:
            break
        if current_points > points:
            points = current_points
            the_most_powerful_word = command
print(f"The most powerful word is {the_most_powerful_word} - {points}")