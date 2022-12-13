def locate_knights(matrix):
    knights = []

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "K":
                knights.append((row, col))

    return knights


def idx_in_matrix(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        if matrix[row][col] == "K":
            return True

    return False


def knight_to_remove(matrix, knights_coordinates):
    knights_with_potential_enemies = {}

    for knight in knights_coordinates:
        enemies = 0
        row, column = knight

        if idx_in_matrix(matrix, row - 2, column + 1):
            enemies += 1

        if idx_in_matrix(matrix, row - 2, column - 1):
            enemies += 1

        if idx_in_matrix(matrix, row - 1, column + 2):
            enemies += 1

        if idx_in_matrix(matrix, row - 1, column - 2):
            enemies += 1

        if idx_in_matrix(matrix, row + 1, column + 2):
            enemies += 1

        if idx_in_matrix(matrix, row + 1, column - 2):
            enemies += 1

        if idx_in_matrix(matrix, row + 2, column + 1):
            enemies += 1

        if idx_in_matrix(matrix, row + 2, column - 1):
            enemies += 1

        if enemies > 0:
            knights_with_potential_enemies[knight] = enemies

    if knights_with_potential_enemies:
        return max(knights_with_potential_enemies, key=knights_with_potential_enemies.get)


size = int(input())
chessboard = [list(input()) for x in range(size)]
knights_coordinates = locate_knights(chessboard)
removed_knights = 0

while True:
    if not knight_to_remove(chessboard, knights_coordinates):
        break

    current_row, current_col = knight_to_remove(chessboard, knights_coordinates)
    knights_coordinates.remove((current_row, current_col))
    chessboard[current_row][current_col] = "0"
    removed_knights += 1

print(removed_knights)
# ===========================================================================================
#
# def valid_index(size, row, col):
#     if 0 <= row < size and 0 <= col < size:
#         return True
#     return False
#
#
# def k_coordinates(matrix):
#     coordinates = []
#     for row in range(len(matrix)):
#         for col in range(len(matrix)):
#             if matrix[row][col] == "K":
#                 coordinates.append((row, col))
#     return coordinates
#
#
# def k_possible_moves(row, column, size):
#     poss_moves = []
#     if valid_index(size, row - 2, column + 1):
#         poss_moves.append((row - 2, column + 1))
#     if valid_index(size, row - 2, column - 1):
#         poss_moves.append((row - 2, column - 1))
#     if valid_index(size, row - 1, column + 2):
#         poss_moves.append((row - 1, column + 2))
#     if valid_index(size, row - 1, column - 2):
#         poss_moves.append((row - 1, column - 2))
#     if valid_index(size, row + 1, column + 2):
#         poss_moves.append((row + 1, column + 2))
#     if valid_index(size, row + 1, column - 2):
#         poss_moves.append((row + 1, column - 2))
#     if valid_index(size, row + 2, column + 1):
#         poss_moves.append((row + 2, column + 1))
#     if valid_index(size, row + 2, column - 1):
#         poss_moves.append((row + 2, column - 1))
#     return poss_moves
#
#
# size = int(input())
# board = [[x for x in list(input())] for y in range(size)]
# knights_coordinates = k_coordinates(board)
#
# removed_knights = 0
# while True:
#     knights_left = {x: 0 for x in knights_coordinates}
#
#     for coords in knights_left.keys():
#         row, col = coords
#         moves = k_possible_moves(row, col, size)
#         for coord in moves:
#             if coord in knights_left:
#                 knights_left[coords] += 1
#
#     knights_left = {k: v for k, v in knights_left.items() if v != 0}
#
#     if not knights_left:
#         break
#
#     max_k = max(knights_left, key=knights_left.get)
#     del knights_left[max_k]
#     knights_coordinates.remove(max_k)
#
#     removed_knights += 1
#
# print(removed_knights)
