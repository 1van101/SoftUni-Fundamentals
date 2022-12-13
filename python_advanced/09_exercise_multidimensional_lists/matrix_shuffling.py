def coordinates_validation(rows, cols, row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True
    print("Invalid input!")
    return False


def swap_the_values(matrix, rows, cols, row1, col1, row2, col2):
    if coordinates_validation(rows, cols, row1, col1) and coordinates_validation(rows, cols, row2, col2):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(' '.join(x)) for x in matrix]
    return matrix


rows, columns = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for y in range(rows)]

command = input()
while not command == "END":
    curr_command = command.split()
    if len(curr_command) == 5 and curr_command[0] == "swap":
        first_row, first_col, second_row, second_col = [int(x) for x in curr_command[1:]]
        matrix = swap_the_values(matrix, rows, columns, first_row, first_col, second_row, second_col)
    else:
        print("Invalid input!")
    command = input()
