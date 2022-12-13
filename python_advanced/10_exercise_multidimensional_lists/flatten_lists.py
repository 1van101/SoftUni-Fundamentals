sub = input().split("|")
new_sub = []

while sub:
    new_sub += sub.pop().split()

print(*new_sub)