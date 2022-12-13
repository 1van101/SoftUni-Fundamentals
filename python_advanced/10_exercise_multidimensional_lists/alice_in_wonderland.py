def locate(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "A":
                return (row, col)


def idxs_in_matrix(size, row, col):
    if 0 <= row < size and 0 <= col < size:
        return True


def step_up(row, col):
    return (row - 1, col)


def step_down(row, col):
    return (row + 1, col)


def step_left(row, col):
    return (row, col - 1)


def step_right(row, col):
    return (row, col + 1)


size = int(input())
field = [input().split() for x in range(size)]
alice_row, alice_col = locate(field)
tea_bags = 0

directions = {
    "up": step_up,
    "down": step_down,
    "left": step_left,
    "right": step_right
}
while True:
    direction = input()

    field[alice_row][alice_col] = "*"

    alice_row, alice_col = directions[direction](alice_row, alice_col)

    if not idxs_in_matrix(size, alice_row, alice_col):
        break

    if field[alice_row][alice_col].isdigit():
        tea_bags += int(field[alice_row][alice_col])

    if field[alice_row][alice_col] == "R" or tea_bags >= 10:
        field[alice_row][alice_col] = "*"
        break

    field[alice_row][alice_col] = "A"

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*x) for x in field]
