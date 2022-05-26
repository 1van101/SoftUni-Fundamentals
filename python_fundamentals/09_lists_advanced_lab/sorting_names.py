names = input().split(", ")
names_sorted = sorted(names, key=lambda x: (-len(x), x))
print(names_sorted)