n, m = input().split()

first_set = {int(input()) for x in range(int(n))}
second_set = {int(input()) for y in range(int(m))}
[print(x) for x in first_set.intersection(second_set)]
