from collections import deque


operations = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x // y
}

expression = deque(input().split())
numbers = deque()

for el in expression:
    if el not in operations:
        numbers.append(int(el))
    else:
        while len(numbers) > 1:
            numbers.appendleft(operations[el](numbers.popleft(), numbers.popleft()))

print(*numbers)