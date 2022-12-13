def indices_are_valid(size, first, second):
    if 0 <= first < size and 0 <= second < size:
        return True
    print("Invalid coordinates")
    return False


def add(matrix, first, second, value):
    if indices_are_valid(len(matrix), first, second):
        matrix[first][second] += value
    return matrix


def subtract(matrix, first, second, value):
    if indices_are_valid(len(matrix), first, second):
        matrix[first][second] -= value
    return matrix


size = int(input())
matrix = [[int(x) for x in input().split()] for y in range(size)]

while True:
    command = input().split()
    if command[0] == "END":
        break
    if command[0] == "Add":
        matrix = add(matrix, int(command[1]), int(command[2]), int(command[3]))
    elif command[0] == "Subtract":
        matrix = subtract(matrix, int(command[1]), int(command[2]), int(command[3]))

[print(' '.join(str(y) for y in matrix[x])) for x in range(size)]
