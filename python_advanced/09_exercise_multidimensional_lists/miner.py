def in_matrix(size, el):
    if 0 <= el < size:
        return True
    return False


def locate_positions(field, size, type):
    coals = []
    for row in range(size):
        for col in range(size):
            if field[row][col] == f"{type}" and type != "c":
                return (row, col)
            elif field[row][col] == f"{type}" and type == "c":
                coals.append((row, col))
    return coals


def move(size, direction, last_position):
    row, col = last_position
    if direction == "up" and in_matrix(size, row - 1):
        row -= 1
    elif direction == "down" and in_matrix(size, row + 1):
        row += 1
    elif direction == "right" and in_matrix(size, col + 1):
        col += 1
    elif direction == "left" and in_matrix(size, col - 1):
        col -= 1
    return (row, col)


size = int(input())
directions = input().split()

matrix = [[x for x in input().split()] for y in range(size)]

miner_location = locate_positions(matrix, size, "s")
end_point = locate_positions(matrix, size, "e")
coals = locate_positions(matrix, size, "c")

for direction in directions:
    miner_location = move(size, direction, miner_location)

    if miner_location == end_point:
        print(f"Game over! {miner_location}")
        exit()
    if miner_location in coals:
        coals.remove(miner_location)
        matrix[miner_location[0]][miner_location[1]] = "*"

if not coals:
    print(f"You collected all coal! {miner_location}")
else:
    print(f"{len(coals)} pieces of coal left. {miner_location}")

# =========================================================================
# def in_matrix(matrix_el, el):
#     if 0 <= el < matrix_el:
#         return True
#     return False
#
#
# def locate(matrix):
#     miner_loc = ()
#     coals_loc = []
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             if matrix[row][col] == "s":
#                 miner_loc = (row, col)
#             elif matrix[row][col] == "c":
#                 coals_loc.append((row, col))
#     return miner_loc, len(coals_loc)
#
# size = int(input())
# commands = input().split()
# matrix = [[x for x in input().split()] for y in range(size)]
#
# miner_location, coals= locate(matrix)
# miner_row, miner_col = miner_location
#
# lost_the_game = False
# for command in commands:
#     if command == "up" and in_matrix(size, miner_row - 1):
#         miner_row -= 1
#     elif command == "down" and in_matrix(size, miner_row + 1):
#         miner_row += 1
#     elif command == "left" and in_matrix(size, miner_col - 1):
#         miner_col -= 1
#     elif command == "right" and in_matrix(size, miner_col + 1):
#         miner_col += 1
#     if matrix[miner_row][miner_col] == "c":
#         matrix[miner_row][miner_col] = "*"
#         coals -= 1
#     elif matrix[miner_row][miner_col] == "e":
#         print(f"Game over! {miner_row, miner_col}")
#         exit()
#
# if coals:
#     print(f"{coals} pieces of coal left. {miner_row, miner_col}")
# else:
#     print(f"You collected all coal! {miner_row, miner_col}")