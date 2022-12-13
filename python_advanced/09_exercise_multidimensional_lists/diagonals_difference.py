n = int(input())
matrix = [[int(x) for x in input().split()] for y in range(n)]

first_diagonal = sum([matrix[x][x] for x in range(n)])
second_diagonal = sum([matrix[x][n - 1 - x] for x in range(n)])

print(abs(first_diagonal - second_diagonal))
