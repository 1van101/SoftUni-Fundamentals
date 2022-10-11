rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for y in range(rows)]
result = sum([sum(x) for x in matrix])

print(result)
print(matrix)