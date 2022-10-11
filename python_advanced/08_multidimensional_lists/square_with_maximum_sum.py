rows, columns = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for y in range(rows)]

all_squares = []

for row in range(rows - 1):
    for col in range(columns - 1):
        all_squares.append([
            matrix[row][col],
            matrix[row][col + 1],
            matrix[row + 1][col],
            matrix[row + 1][col + 1]
        ])

final_res = {x: sum(y) for x, y in enumerate(all_squares)}
max_result = max(final_res, key= final_res.get)
highest_pair = all_squares[max_result]

[print(f"{highest_pair[i]} {highest_pair[i + 1]}") for i in range(0, len(highest_pair), 2)]
print(final_res[max_result])

# ==========================================================================================================================
#
# import sys
#
# rows, columns = [int(x) for x in input().split(", ")]
# matrix = [[int(x) for x in input().split(", ")] for y in range(rows)]
#
# max_sum_square = []
# max_sum = -sys.maxsize
#
# for row in range(rows - 1):
#     for column in range(columns - 1):
#         current_square = [matrix[row][column], matrix[row][column + 1], matrix[row + 1][column], matrix[row + 1][column + 1]]
#         if sum(current_square) > max_sum:
#             max_sum = sum(current_square)
#             max_sum_square = current_square.copy()
#
# [print(f"{max_sum_square[x]} {max_sum_square[x + 1]}") for x in range(0, len(max_sum_square), 2)]
# print(sum(max_sum_square))

