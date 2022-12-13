def locate(matrix, type):
    targets = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "A" and type == "A":
                return (row, col)
            elif matrix[row][col] == "x" and type == "x":
                targets.append((row, col))
    return targets


def shoot_up(row, col, steps):
    return (row - steps, col)


def shoot_down(row, col, steps):
    return (row + steps, col)


def shoot_left(row, col, steps):
    return (row, col - steps)


def shoot_right(row, col, steps):
    return (row, col + steps)


shotgun_range = [input().split() for x in range(5)]
N = int(input())

shooter = locate(shotgun_range, "A")
targets = locate(shotgun_range, "x")
removed_targets = []

shoot_dirs = {
    "up": shoot_up,
    "down": shoot_down,
    "left": shoot_left,
    "right": shoot_right
}
for _ in range(N):
    if not targets:
        break

    command = input().split()
    action = command[0]

    if action == "shoot":
        shooter_row, shooter_col = shooter

        while shooter_row in range(5) and shooter_col in range(5):
            shooter_row, shooter_col = shoot_dirs[command[1]](shooter_row, shooter_col, 1)
            if (shooter_row, shooter_col) in targets:
                targets.remove((shooter_row, shooter_col))
                removed_targets.append([shooter_row, shooter_col])
                shotgun_range[shooter_row][shooter_col] = "."
                break

    elif action == "move":
        dir = command[1]
        shooter_row, shooter_col = shoot_dirs[dir](shooter[0], shooter[1], int(command[2]))

        if shooter_row in range(5) and shooter_col in range(5):
            if shotgun_range[shooter_row][shooter_col] == ".":
                shotgun_range[shooter[0]][shooter[1]] = "."
                shooter = (shooter_row, shooter_col)
                shotgun_range[shooter_row][shooter_col] = "A"

if targets:
    print(f"Training not completed! {len(targets)} targets left.")
else:
    print(f"Training completed! All {len(removed_targets)} targets hit.")
[print(x) for x in removed_targets]

# =====================================================================================================================
#
# def create_field_and_locate():
#     shooter_loc = tuple()
#     targets_loc = []
#     matrix = []
#
#     for row in range(5):
#         current_row = input().split()
#         for col in range(5):
#             if current_row[col] == "A":
#                 shooter_loc = (row, col)
#             elif current_row[col] == "x":
#                 targets_loc.append([row, col])
#         matrix.append(current_row)
#
#     return matrix, targets_loc, shooter_loc
#
#
# def index_is_valid(row, col):
#     if 0 <= row < 5 and 0 <= col < 5:
#         return True
#
#     return False
#
#
# def move(matrix, direction, row, col, steps):
#     if direction == "up" and index_is_valid(row - steps, col):
#         if matrix[row - steps][col] == ".":
#             matrix[row][col] = "."
#             row = row - steps
#             matrix[row][col] = "A"
#     elif direction == "down" and index_is_valid(row + steps, col):
#         if matrix[row + steps][col] == ".":
#             matrix[row][col] = "."
#             row = row + steps
#             matrix[row][col] = "A"
#     elif direction == "left" and index_is_valid(row, col - steps):
#         if matrix[row][col - steps] == ".":
#             matrix[row][col] = "."
#             col = col - steps
#             matrix[row][col] = "A"
#     elif direction == "right" and index_is_valid(row, col + steps):
#         if matrix[row][col + steps] == ".":
#             matrix[row][col] = "."
#             col = col + steps
#             matrix[row][col] = "A"
#     return matrix, row, col
#
#
# def shoot(matrix, direction, row, col, targets, shot_targets):
#     while True:
#         if direction == "up":
#             if not index_is_valid(row - 1, col):
#                 break
#             row = row - 1
#             if [row, col] in targets:
#                 targets.remove([row, col])
#                 shot_targets.append([row, col])
#                 matrix[row][col] = "."
#                 break
#         elif direction == "down":
#             if not index_is_valid(row + 1, col):
#                 break
#             row = row + 1
#             if [row, col] in targets:
#                 targets.remove([row, col])
#                 shot_targets.append([row, col])
#                 matrix[row][col] = "."
#                 break
#         elif direction == "left":
#             if not index_is_valid(row, col - 1):
#                 break
#             col = col - 1
#             if [row, col] in targets:
#                 targets.remove([row, col])
#                 shot_targets.append([row, col])
#                 matrix[row][col] = "."
#                 break
#         elif direction == "right":
#             if not index_is_valid(row, col + 1):
#                 break
#             col = col + 1
#             if [row, col] in targets:
#                 targets.remove([row, col])
#                 shot_targets.append([row, col])
#                 matrix[row][col] = "."
#                 break
#     return matrix, targets, shot_targets
#
#
# field, targets, shooter = create_field_and_locate()
# shooter_row, shooter_col = shooter
# number_of_commands = int(input())
# shot_targets = []
# for _ in range(number_of_commands):
#     command = input().split()
#     action = command[0]
#     if action == "move":
#         field, shooter_row, shooter_col = move(field, command[1], shooter_row, shooter_col, int(command[2]))
#     elif action == "shoot":
#         field, targets, shot_targets = shoot(field, command[1], shooter_row, shooter_col, targets, shot_targets)
#     if not targets:
#         break
#
# if targets:
#     print(f"Training not completed! {len(targets)} targets left.")
# else:
#     print(f"Training completed! All {len(shot_targets)} targets hit.")
# [print(x) for x in shot_targets]
