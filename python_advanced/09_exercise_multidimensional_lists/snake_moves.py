rows, columns = [int(x) for x in input().split()]
snake = input()

matrix = [["" for x in range(columns)] for y in range(rows)]

letter_number = 0

for row in range(rows):
    for column in range(columns):
        matrix[row][column] = snake[letter_number % len(snake)]
        letter_number += 1
    if row % 2 == 0:
        print(''.join(matrix[row]))
    else:
        print(''.join(reversed(matrix[row])))
