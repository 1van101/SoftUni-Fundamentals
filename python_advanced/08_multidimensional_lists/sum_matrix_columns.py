rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split()] for y in range(rows)]

sum_of_columns_els = [sum(x[y] for x in matrix) for y in range(cols)]

print(*sum_of_columns_els, sep="\n")
# =========================================================================
# rows, columns = [int(x) for x in input().split(", ")]
# matrix = [[int(x) for x in input().split()] for y in range(rows)]
#
# for column in range(columns):
#     sum = 0
#     for row in range(rows):
#         sum += matrix[row][column]
#     print(sum)
