def create_and_locate(N):
    player = tuple()
    bunnies = set()
    field = []

    for row in range(N):
        current_row = list(input())
        field.append(current_row)
        for col in range(len(current_row)):
            if current_row[col] == "P":
                player = (row, col)
            elif current_row[col] == "B":
                bunnies.add((row, col))

    return field, player, bunnies


def in_field(N, M, row, col):
    return all([row in range(N), col in range(M)])


def move_up(row, col):
    return row - 1, col


def move_down(row, col):
    return row + 1, col


def move_left(row, col):
    return row, col - 1


def move_right(row, col):
    return row, col + 1


def spreading_bunnies(matrix, N, M, bunnies):
    new_bunnies = bunnies.copy()

    for bunny in bunnies:
        row, col = bunny

        surrounding_cells = [
            move_up(row, col),
            move_down(row, col),
            move_left(row, col),
            move_right(row, col)
        ]

        for cell in surrounding_cells:
            if in_field(N, M, cell[0], cell[1]):
                new_bunnies.add((cell[0], cell[1]))
                matrix[cell[0]][cell[1]] = "B"

    return new_bunnies


N, M = [int(x) for x in input().split()]

field, player, bunnies = create_and_locate(N)

directions = {
    "U": move_up,
    "D": move_down,
    "L": move_left,
    "R": move_right
}
won = False
commands = list(input())

for direction in commands:
    field[player[0]][player[1]] = "."
    player_next_move = directions[direction](player[0], player[1])

    bunnies = spreading_bunnies(field, N, M, bunnies)

    if not in_field(N, M, player_next_move[0], player_next_move[1]):
        won = True
        break

    if player_next_move in bunnies:
        break

    field[player_next_move[0]][player_next_move[1]] = "P"
    player = player_next_move

[print(''.join(x)) for x in field]
if won:
    print(f"won: {' '.join(str(x) for x in player)}")
else:
    print(f"dead: {' '.join(str(x) for x in player_next_move)}")
