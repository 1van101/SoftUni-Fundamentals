number_of_lines = int(input())
squares = []
counter = 0

for line in range(number_of_lines):
    current_squares = [int(x) for x in input().split()]
    squares.append(current_squares)

attacks = input().split()

for attack in attacks:
    row = int(attack[0])
    col = int(attack[2])
    if squares[row][col] != 0:
        squares[row][col] -= 1
        if squares[row][col] == 0:
            counter += 1

print(counter)