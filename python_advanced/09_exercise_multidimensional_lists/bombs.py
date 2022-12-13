def is_valid_index(size, row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def get_the_surrounding_cells(matrix, size, row, col, explosion):
    if is_valid_index(size, row - 1, col - 1) and matrix[row - 1][col - 1] > 0:
        matrix[row - 1][col - 1] -= explosion
    if is_valid_index(size, row - 1, col) and matrix[row - 1][col] > 0:
        matrix[row - 1][col] -= explosion
    if is_valid_index(size, row - 1, col + 1) and matrix[row - 1][col + 1] > 0:
        matrix[row - 1][col + 1] -= explosion
    if is_valid_index(size, row, col - 1) and matrix[row][col - 1] > 0:
        matrix[row][col - 1] -= explosion
    if is_valid_index(size, row, col + 1) and matrix[row][col + 1] > 0:
        matrix[row][col + 1] -= explosion
    if is_valid_index(size, row + 1, col - 1) and matrix[row + 1][col - 1] > 0:
        matrix[row + 1][col - 1] -= explosion
    if is_valid_index(size, row + 1, col) and matrix[row + 1][col] > 0:
        matrix[row + 1][col] -= explosion
    if is_valid_index(size, row + 1, col + 1) and matrix[row + 1][col + 1] > 0:
        matrix[row + 1][col + 1] -= explosion
    return matrix


size = int(input())
matrix = [[int(x) for x in input().split()] for y in range(size)]
bombs_coordinates = input().split()
for coordinate in bombs_coordinates:
    curr_row, curr_col = [int(x) for x in coordinate.split(",")]
    explosion = matrix[curr_row][curr_col]

    if explosion > 0:
        matrix[curr_row][curr_col] = 0
        matrix = get_the_surrounding_cells(matrix, size, curr_row, curr_col, explosion)

alive_cells = 0
sum = 0

for row in matrix:
    for num in row:
        if num > 0:
            alive_cells += 1
            sum += num

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum}")
[print(' '.join(str(y) for y in x)) for x in matrix]
