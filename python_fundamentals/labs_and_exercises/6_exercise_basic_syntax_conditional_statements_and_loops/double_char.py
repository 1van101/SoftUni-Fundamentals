while True:
    word = input()
    if word == "End":
        break
    [print(x * 2, end="") for x in word if word != "SoftUni"]
    print()
