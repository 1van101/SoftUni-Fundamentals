def get_squares(matrix, rows, cols):
    equal_squares = 0
    for row in range(rows - 1):
        for col in range(cols - 1):
            if all([matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]]):
                equal_squares += 1
    return equal_squares


rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for y in range(rows)]
squares = get_squares(matrix, rows, cols)
print(squares)