even_set = set()
odd_set = set()

n = int(input())

for i in range(1, n + 1):
    current_sum = sum([ord(x) for x in input()]) // i
    even_set.add((current_sum)) if current_sum % 2 == 0 else odd_set.add(current_sum)

if sum(even_set) == sum(odd_set):
    res = even_set.union(odd_set)
elif sum(even_set) < sum(odd_set):
    res = odd_set.difference(even_set)
else:
    res = odd_set.symmetric_difference(even_set)
print(*res, sep=", ")