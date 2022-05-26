numbers = [int(x) for x in input().split(", ")]
beggars = int(input())
numbers_filtered = []
counter = 0

while counter < beggars:
    temp_sum = 0
    for num in range(counter, len(numbers), beggars):
        temp_sum += numbers[num]
    counter += 1
    numbers_filtered.append(temp_sum)
print(numbers_filtered)