# while True:
#
#     command = input()
#     if command == "End":
#         break
#     elif command == "SoftUni":
#         continue
#     for letter in command:
#         print(letter * 2, end="")
#     print()



while True:
    word = input()
    if word == "End":
        break
    [print(x * 2, end="") for x in word if word != "SoftUni"]
    print()
