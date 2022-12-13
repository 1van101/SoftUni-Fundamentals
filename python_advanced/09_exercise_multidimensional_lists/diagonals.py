rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for y in range(rows)]
first_diagonal = [matrix[x][x] for x in range(rows)]
second_diagonal = [matrix[x][rows - 1 - x] for x in range(rows)]

print(f"Primary diagonal: {', '.join([str(x) for x in first_diagonal])}. Sum: {sum(first_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in second_diagonal])}. Sum: {sum(second_diagonal)}")

#===============================================================================================================
# def add_diagonals(n):
#     primary = []
#     secondary = []
#     for i in range(n):
#         primary.append(matrix[i][i])
#         secondary.append(matrix[i][n - 1 - i])
#     return primary, secondary
#
#
# matrix_size = int(input())
# matrix = [[int(x) for x in input().split(", ")] for y in range(matrix_size)]
# primary_diagonal, secondary_diagonal = add_diagonals(matrix_size)
#
#
# print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")