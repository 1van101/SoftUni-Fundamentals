def locate(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "B":
                return (row, col)


def vertically(matrix, dir, row, col):
    paths = []
    eggs = 0

    if dir == "up":
        while (row - 1) in range(len(matrix)):
            row -= 1
            if matrix[row][col] == "X":
                break
            paths.append([row, col])
            eggs += int(matrix[row][col])
    elif dir == "down":
        while (row + 1) in range(len(matrix)):
            row += 1
            if matrix[row][col] == "X":
                break
            paths.append([row, col])
            eggs += int(matrix[row][col])

    return {"eggs": eggs, "paths": paths}


def horizontally(matrix, dir, row, col):
    paths = []
    eggs = 0

    if dir == "left":
        while (col - 1) in range(len(matrix)):
            col -= 1
            if matrix[row][col] == "X":
                break
            paths.append([row, col])
            eggs += int(matrix[row][col])
    elif dir == "right":
        while (col + 1) in range(len(matrix)):
            col += 1
            if matrix[row][col] == "X":
                break
            paths.append([row, col])
            eggs += int(matrix[row][col])

    return {"eggs": eggs, "paths": paths}


size = int(input())
field = [input().split() for x in range(size)]

bunny_row, bunny_col = locate(field)
bunny_and_eggs = {
    "up": vertically(field, "up", bunny_row, bunny_col),
    "down": vertically(field, "down", bunny_row, bunny_col),
    "left": horizontally(field, "left", bunny_row, bunny_col),
    "right": horizontally(field, "right", bunny_row, bunny_col)
}
bunny_and_eggs_filtered = {k:v for k, v in bunny_and_eggs.items() if len(bunny_and_eggs[k]["paths"]) > 0}

dir_max_eggs = max(bunny_and_eggs_filtered.keys(), key=lambda x: bunny_and_eggs_filtered[x]["eggs"])
print(dir_max_eggs)
[print(x) for x in bunny_and_eggs_filtered[dir_max_eggs]["paths"]]
print(bunny_and_eggs_filtered[dir_max_eggs]["eggs"])


# ========================================================================================

# def move_up(row, col):
#     return row - 1, col
#
#
# def move_down(row, col):
#     return row + 1, col
#
#
# def move_left(row, col):
#     return row, col - 1
#
#
# def move_right(row, col):
#     return row, col + 1
#
#
# size = int(input())
# matrix = []
# bunny_row, bunny_col = 0, 0
#
# for row in range(size):
#     row_el = input().split()
#     matrix.append(row_el)
#
#     for col in range(size):
#         if row_el[col] == "B":
#             bunny_row = row
#             bunny_col = col
#
# directions = {
#     "up": move_up,
#     "down": move_down,
#     "left": move_left,
#     "right": move_right
# }
# best_score = float('-inf')
# best_dir = ""
# best_path = []
# for direction, step in directions.items():
#     current_row, current_col = bunny_row, bunny_col
#     current_score = 0
#     path = []
#
#     while True:
#         current_row, current_col = step(current_row, current_col)
#
#         if current_row < 0 or current_col < 0 or current_row >= size or current_col >= size:
#             break
#
#         if matrix[current_row][current_col] == "X":
#             break
#
#         path.append([current_row, current_col])
#         current_score += int(matrix[current_row][current_col])
#
#     if current_score > best_score and path:
#         best_score = current_score
#         best_dir = direction
#         best_path = path
#
# print(best_dir)
# [print(x) for x in best_path]
# print(best_score)
