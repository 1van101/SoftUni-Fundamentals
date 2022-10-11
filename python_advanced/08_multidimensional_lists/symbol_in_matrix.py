n = int(input())

matrix = [[x for x in list(input())] for y in range(n)]
symbol = input()

for row in range(n):
    for column in range(n):
        if matrix[row][column] == symbol:
            print((row, column))
            exit()
print(f"{symbol} does not occur in the matrix")