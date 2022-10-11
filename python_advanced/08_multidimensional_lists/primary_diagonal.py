n = int(input())
matrix = [[int(x) for x in input().split()] for y in range(n)]
primary_diagonal = sum([matrix[x][x] for x in range(n)])
print(sum([matrix[x][x] for x in range(n)]))
