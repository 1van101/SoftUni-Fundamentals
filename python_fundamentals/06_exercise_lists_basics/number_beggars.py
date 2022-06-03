numbers = [int(x) for x in input().split(", ")]
beggars = int(input())
numbers_filtered = []
counter = 0

while counter < beggars:
    sum = 0
    for num in range(counter, len(numbers), beggars):
        sum += numbers[num]
    counter += 1
    numbers_filtered.append(sum)
print(numbers_filtered)