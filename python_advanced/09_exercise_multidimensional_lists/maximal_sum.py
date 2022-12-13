import sys


def check_for_squares(matrix, r, c):
    max_square = []
    max_res = - sys.maxsize
    for row in range(r - 2):
        for col in range(c - 2):
            current_square = [
                matrix[row][col], matrix[row][col + 1], matrix[row][col + 2],
                matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2],
                matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]
            ]
            current_sum = sum(current_square)
            if current_sum > max_res:
                max_res = current_sum
                max_square = current_square
    return max_res, max_square


rows, cols = [int(x) for x in input().split()]
matrix_nums = [[int(x) for x in input().split()] for y in range(rows)]

max_result, max_square = check_for_squares(matrix_nums, rows, cols)

print(f"Sum = {max_result}")
[print(f"{max_square[x]} {max_square[x + 1]} {max_square[x + 2]}") for x in range(0, len(max_square), 3)]