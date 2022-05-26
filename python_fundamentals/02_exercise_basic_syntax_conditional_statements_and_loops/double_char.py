while True:
    word = input()
    if word == "End":
        break
    elif word == "SoftUni":
        continue
    [print(x * 2, end="") for x in word]
    print()
