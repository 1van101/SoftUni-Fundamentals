def locate(matrix, object):
    nice_kids = []
    naughty_kids = []

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "S" and object == "S":
                return (row, col)
            elif matrix[row][col] == "V" and object == "V":
                nice_kids.append((row, col))
            elif matrix[row][col] == "X" and object == "X":
                naughty_kids.append((row, col))

    if object == "V":
        return nice_kids

    if object == "X":
        return naughty_kids


def move_up(row, col):
    return (row - 1, col)


def move_down(row, col):
    return (row + 1, col)


def move_left(row, col):
    return (row, col - 1)


def move_right(row, col):
    return (row, col + 1)


def check_cells_around(matrix, nice, naughty, santa):
    global presents
    for dir in directions.values():
        r, c = dir(santa[0], santa[1])
        if (r, c) in naughty:
            naughty.remove((r, c))
            presents -= 1
            matrix[r][c] = "-"
        elif (r, c) in nice:
            nice.remove((r, c))
            presents -= 1
            matrix[r][c] = "-"
        if not presents and nice:
            break
    return matrix


presents = int(input())
size = int(input())
neighborhood = [input().split() for x in range(size)]

santa_loc = locate(neighborhood, "S")
nice_kids = locate(neighborhood, "V")
naughty_kids = locate(neighborhood, "X")

count_nice_kids = len(nice_kids)

directions = {
    "up": move_up,
    "down": move_down,
    "left": move_left,
    "right": move_right
}

while presents and nice_kids:
    dir = input()

    if dir == "Christmas morning":
        break

    neighborhood[santa_loc[0]][santa_loc[1]] = "-"
    current_loc_santa = directions[dir](santa_loc[0], santa_loc[1])
    current_row, current_col = current_loc_santa

    if current_loc_santa in nice_kids:
        nice_kids.remove(current_loc_santa)
        presents -= 1
    elif current_loc_santa in naughty_kids:
        naughty_kids.remove(current_loc_santa)
    elif neighborhood[current_row][current_col] == "C":
        neighborhood = check_cells_around(neighborhood, nice_kids, naughty_kids, current_loc_santa)

    neighborhood[current_row][current_col] = "S"
    santa_loc = current_loc_santa

if not presents and nice_kids:
    print("Santa ran out of presents!")
[print(" ".join(x)) for x in neighborhood]
if not nice_kids:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {len(nice_kids)} nice kid/s.")

# ================================================================================
#
#
# def get_coordinates(size):
#     santa = tuple()
#     for row in range(size):
#         current_row = input().split()
#         neighborhood.append(current_row)
#         for col in range(size):
#             if current_row[col] == "S":
#                 santa = (row, col)
#             elif current_row[col] == "X":
#                 naughty_kids.append((row, col))
#             elif current_row[col] == "V":
#                 nice_kids.append((row, col))
#             elif current_row[col] == "C":
#                 cookies.append((row, col))
#     return santa
#
#
# def is_valid_index(matrix, row, col):
#     if 0 <= row < len(matrix) and 0 <= col < len(matrix):
#         return True
#     return False
#
#
# def move_up(matrix, row, col):
#     if is_valid_index(matrix, row - 1, col):
#         return matrix[row - 1][col]
#
#
# def move_down(matrix, row, col):
#     if is_valid_index(matrix, row + 1, col):
#         return matrix[row + 1][col]
#
#
# def move_left(matrix, row, col):
#     if is_valid_index(matrix, row, col - 1):
#         return matrix[row][col - 1]
#
#
# def move_right(matrix, row, col):
#     if is_valid_index(matrix, row, col + 1):
#         return matrix[row][col + 1]
#
#
# presents = int(input())
# neighborhood_size = int(input())
#
# neighborhood = []
# naughty_kids = []
# nice_kids = []
# cookies = []
#
#
# santa_coordinates = get_coordinates(neighborhood_size)
#
# nice_kids_number = len(nice_kids)
# out_of_presents = False
#
# directions = {
#     "up": move_up,
#     "down": move_down,
#     "left": move_left,
#     "right": move_right
# }
# santa_row, santa_col = santa_coordinates
# command = input()
# while not command == "Christmas morning":
#     if presents <= 0:
#         out_of_presents = True
#         break
#     neighborhood[santa_row][santa_col] = "-"
#     if command == 'up':
#         # directions['up'](neighborhood, santa_row, santa_col)
#         santa_row = santa_row - 1
#     elif command == "down":
#         # directions['down'](neighborhood, santa_row, santa_col)
#         santa_row = santa_row + 1
#     elif command == "left":
#         # directions['left'](neighborhood, santa_row, santa_col)
#         santa_col = santa_col - 1
#     elif command == "right":
#         # directions['right'](neighborhood, santa_row, santa_col)
#         santa_col = santa_col + 1
#     neighborhood[santa_row][santa_col] = "S"
#     if (santa_row, santa_col) in nice_kids:
#         nice_kids.remove((santa_row, santa_col))
#         presents -= 1
#     if (santa_row, santa_col) in cookies:
#         cookies.remove((santa_row, santa_col))
#         if (santa_row - 1, santa_col) in nice_kids:
#             nice_kids.remove((santa_row -1, santa_col))
#             presents -= 1
#         elif (santa_row - 1, santa_col) in naughty_kids:
#             naughty_kids.remove((santa_row - 1, santa_col))
#             neighborhood[santa_row - 1][santa_col] = "-"
#             presents -= 1
#         if presents <= 0:
#             out_of_presents = True
#             break
#         if (santa_row + 1, santa_col) in nice_kids:
#             nice_kids.remove((santa_row +1, santa_col))
#             presents -= 1
#         elif (santa_row + 1, santa_col) in naughty_kids:
#             naughty_kids.remove((santa_row + 1, santa_col))
#             presents -= 1
#         neighborhood[santa_row + 1][santa_col] = "-"
#         if presents <= 0:
#             out_of_presents = True
#             break
#         if (santa_row, santa_col - 1) in nice_kids:
#             nice_kids.remove((santa_row, santa_col - 1))
#             presents -= 1
#         elif (santa_row, santa_col - 1) in naughty_kids:
#             naughty_kids.remove((santa_row, santa_col - 1))
#             presents -= 1
#         neighborhood[santa_row][santa_col - 1] = "-"
#         if presents <= 0:
#             out_of_presents = True
#             break
#         if (santa_row, santa_col + 1) in nice_kids:
#             nice_kids.remove((santa_row, santa_col + 1))
#             presents -= 1
#         elif (santa_row, santa_col + 1) in naughty_kids:
#             naughty_kids.remove((santa_row, santa_col + 1))
#             presents -= 1
#         neighborhood[santa_row][santa_col + 1] = "-"
#         if presents <= 0:
#             out_of_presents = True
#             break
#         # directions['up'](neighborhood, santa_row - 1, santa_col)
#         # directions['down'](neighborhood, santa_row + 1, santa_col)
#         # directions['left'](neighborhood, santa_row, santa_col - 1)
#         # directions['right'](neighborhood, santa_row, santa_col + 1)
#
#     command = input()
#
# if out_of_presents:
#     print("Santa ran out of presents!")
#
# [print(' '.join(x)) for x in neighborhood]
#
# if not nice_kids:
#     print(f"Good job, Santa! {nice_kids_number} happy nice kid/s.")
# else:
#     print(f"No presents for {len(nice_kids)} nice kid/s.")