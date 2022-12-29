def create_and_locate():
    size = int(input())
    matrix = []
    pl = []
    for row in range(size):
        curr_row = input().split()
        if "P" in curr_row:
            pl = [row, curr_row.index("P")]
        matrix.append(curr_row)
    return matrix, pl


def move_up(row, col):
    return [(row - 1) % len(board), col]


def move_down(row, col):
    return [(row + 1) % len(board), col]


def move_left(row, col):
    return [row, (col - 1) % len(board)]


def move_right(row, col):
    return [row, (col + 1) % len(board)]


GOAL = 100
coins = 0

hit_wall = False
parity = ("You won!", "Game over!")

board, player_loc = create_and_locate()

path = [player_loc]
directions = {
    "up": move_up,
    "down": move_down,
    "left": move_left,
    "right": move_right
}

while coins < GOAL:
    command = input()
    player_loc = directions[command](player_loc[0], player_loc[1])

    if player_loc not in path:
        try:
            coins += int(board[player_loc[0]][player_loc[1]])
        except ValueError:
            path.append(player_loc)
            hit_wall = True
            coins //= 2
            break
    path.append(player_loc)

print(f"{parity[hit_wall]} You've collected {coins} coins.\nYour path:")
[print(x) for x in path]
