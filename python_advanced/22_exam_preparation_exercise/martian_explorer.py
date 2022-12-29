def create_and_locate(S):
    pl = []
    matrix = []
    for row in range(S):
        row_input = input().split()
        matrix.append(row_input)
        if "E" in row_input:
            pl = [row, row_input.index("E")]
    return matrix, pl


def move_up(row, col):
    return [(row - 1) % len(matrix), col]


def move_down(row, col):
    return [(row + 1) % len(matrix), col]


def move_left(row, col):
    return [row, (col - 1) % len(matrix)]


def move_right(row, col):
    return [row, (col + 1) % len(matrix)]


SIZE = 6

deposits = {
    "W": {"type": "Water deposit", "qty": 0},
    "M": {"type": "Metal deposit", "qty": 0},
    "C": {"type": "Concrete deposit", "qty": 0}
}

directions = {
    "up": move_up,
    "down": move_down,
    "left": move_left,
    "right": move_right
}

matrix, player = create_and_locate(SIZE)
commands = input().split(", ")

for command in commands:
    player = directions[command](player[0], player[1])
    row, col = player
    on_matrix = matrix[row][col]

    try:
        deposits[on_matrix]["qty"] += 1
        print(f"{deposits[on_matrix]['type']} found at ({row}, {col})")
    except KeyError:
        if on_matrix == "R":
            print(f"Rover got broken at ({row}, {col})")
            break

deposits = len({k: v for k, v in deposits.items() if v["qty"] >= 1})
status_of_area = "suitable" if deposits == 3 else "not suitable"

print(f"Area {status_of_area} to start the colony.")
