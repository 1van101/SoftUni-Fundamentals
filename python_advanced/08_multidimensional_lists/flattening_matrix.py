rows = int(input())

numbers = []
for _ in range(rows):
    nums = [int(x) for x in input().split(', ')]
    numbers.extend(nums)
print(numbers)


# ====================================================================
# rows = int(input())
# matrix = [[int(x) for x in input().split(", ")] for y in range(rows)]
# flattened_matrix = [x for y in matrix for x in y]
# print(flattened_matrix)