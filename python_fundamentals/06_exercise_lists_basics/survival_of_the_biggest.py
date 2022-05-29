numbers = [int(x) for x in input().split()]
lines = int(input())
for num in range(lines):
    numbers.remove(min(numbers))
print(", ".join(map(str, numbers)))
