numbers = []
for num in range(3):
    numbers.append((input()))
numbers = [int(x) for x in numbers]
print(max(numbers))