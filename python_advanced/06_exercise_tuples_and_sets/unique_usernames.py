names = set()
n = int(input())

for i in range(n):
    names.add(input())

[print(x) for x in names]