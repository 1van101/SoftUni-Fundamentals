from colorama import Fore, Style


class FullColumnError(Exception):
    pass


class InvalidIndexError(Exception):
    pass


def player_choice_is_valid(matrix, col):
    matrix_cols = len(matrix[0])
    return col in range(matrix_cols)


def starting_game(R, C):
    matrix = [['0' for y in range(C)] for x in range(R)]
    turns = 0
    print()
    [print(' '.join(matrix[x])) for x in range(R)]
    return matrix, turns


def matrix_is_full(matrix):
    matrix_cols = len(matrix[0])
    return all([matrix[0][x] != "0" for x in range(matrix_cols)])


def color_pl_turn(matrix, pl1, pl2):
    print()
    for row in matrix:
        for cell in row:
            if cell == pl1:
                cell = Fore.BLUE + cell + Fore.RESET
            elif cell == pl2:
                cell = Fore.YELLOW + cell + Fore.RESET
            print(cell, end=" ")
        print()
    print()


def player_turn(matrix, col, curr_pl_sign, pl1, pl2):
    if player_choice_is_valid(matrix, col):
        for r in range(len(matrix) - 1, -1, -1):
            if matrix[r][col] == '0':
                matrix[r][col] = curr_pl_sign
                color_pl_turn(matrix, pl1, pl2)
                return r, col
        else:
            raise FullColumnError
    raise InvalidIndexError


def cell_matches(matrix, row, col, pl_sign):
    if col < 0 or row < 0:
        return False
    try:
        if matrix[row][col] == pl_sign:
            return True
    except IndexError:
        return False
    return False


def vertical(matrix, row, col, pl_sign, win_num):
    try:
        return all([True if matrix[row + i][col] == pl_sign else False for i in range(win_num)])
    except IndexError:
        return False


def horizontal(matrix, row, col, pl_sign, win_num):
    matches = set()

    for i in range(win_num):
        if cell_matches(matrix, row, col + i, pl_sign):
            matches.add((row, col + i))
        else:
            break

    for i in range(win_num):
        if cell_matches(matrix, row, col - i, pl_sign):
            matches.add((row, col - i))
        else:
            break
    return len(matches) >= win_num


def descending_diagonal(matrix, row, col, pl_sign, win_num):
    matches = set()

    for i in range(win_num):
        if cell_matches(matrix, row - i, col - i, pl_sign):
            matches.add((row - i, col - i))
        else:
            break

    for i in range(win_num):
        if cell_matches(matrix, row + i, col + i, pl_sign):
            matches.add((row + i, col + i))
        else:
            break

    return len(matches) >= win_num


def ascending_diagonal(matrix, row, col, pl_sign, win_num):
    matches = set()

    for i in range(win_num):
        if cell_matches(matrix, row - i, col + i, pl_sign):
            matches.add((row - i, col + i))
        else:
            break

    for i in range(win_num):
        if cell_matches(matrix, row + i, col - i, pl_sign):
            matches.add((row + i, col - i))
        else:
            break

    return len(matches) >= win_num


def player_wins(matrix, row, col, pl_sign, win_num):
    return any([
        vertical(matrix, row, col, pl_sign, win_num),
        horizontal(matrix, row, col, pl_sign, win_num),
        ascending_diagonal(matrix, row, col, pl_sign, win_num),
        descending_diagonal(matrix, row, col, pl_sign, win_num)
    ])


def play_again():
    pl_choice = input("Do you want to play again?[Y/N]: ").lower()

    while True:
        if pl_choice == "y" or pl_choice == "n":
            return True if pl_choice == "y" else False
        else:
            print(Fore.RED + "The command should be only [Y/N]! Try again!\n" + Fore.RESET)
        pl_choice = input().lower()


def play():
    ROWS, COLS = 6, 7
    WINNING_NUM = 4
    first_player = input("Please enter a sign for the first player: ").upper()
    second_player = input("Please enter a sign for the second player: ").upper()

    board, turns = starting_game(ROWS, COLS)

    while True:

        game_over = False
        turns += 1
        current_player_sign = second_player if turns % 2 == 0 else first_player

        try:
            player_choice_col = int(input(f"\n{Style.RESET_ALL}PLayer {current_player_sign},"
                                          f" please enter a number of column in range (1 - {COLS}): ")) - 1

            player_row, player_col = \
                player_turn(board, player_choice_col, current_player_sign, first_player, second_player)

            if player_wins(board, player_row, player_col, current_player_sign, WINNING_NUM):
                print(Fore.GREEN + f"The winner is PLAYER {current_player_sign}" + Fore.RESET + "\n")
                game_over = True

            if matrix_is_full(board):
                print(Fore.RED + "The board is full, the game is over, nobody wins!" + Fore.RESET)
                game_over = True

        except FullColumnError:
            print(Fore.RED + "This column is full. Please try with another column next time!" + Fore.RESET)
        except InvalidIndexError:
            print(Fore.RED + "Please enter valid column next time!" + Fore.RESET)
        except ValueError:
            print(Fore.RED + "Your choice must be an integer in given range only!" + Fore.RESET)

        if game_over:
            if play_again():
                board, turns = starting_game(ROWS, COLS)
            else:
                print("Hope to see you soon")
                break


if __name__ == "__main__":
    play()
