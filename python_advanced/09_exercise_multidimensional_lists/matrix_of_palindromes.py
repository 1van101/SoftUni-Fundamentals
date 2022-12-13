rows, columns = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    for column in range(row, row + columns):
        matrix.append(f"{chr(row + 97)}{chr(column + 97)}{chr(row + 97)}")

[print(' '.join(matrix[x:x + columns])) for x in range(0, len(matrix), columns)]

# ====================================================================================
# rows, cols = [int(x) for x in input().split()]
#
# matrix_with_palindromes = [["" for x in range(cols)] for y in range(rows)]
# for row in range(rows):
#     for col in range(cols):
#         matrix_with_palindromes[row][col] = ((f"{chr(97 + row)}{chr(97 + col + row)}{chr(97 + row)}"))
# [print(" ".join(x)) for x in matrix_with_palindromes]