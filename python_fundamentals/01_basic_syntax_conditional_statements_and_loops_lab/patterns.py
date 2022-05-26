number = int(input())
for r in range(1, number + 1):
    for c in range(1, r + 1):
        print("*", end="")
    print()
for r in range(number - 1, 0, -1):
    for c in range(r, 0, -1):
        print("*", end="")
    print()
