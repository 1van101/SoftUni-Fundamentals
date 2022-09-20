n = int(input())
stack = []
for _ in range(n):
    command = input().split()
    if command[0] == "1":
        stack.append(int(command[1]))
    else:
        if stack:
            if command[0] == "2":
                stack.pop()
            elif command[0] == "3":
                print(max(stack))
            elif command[0] == "4":
                print(min(stack))

while stack:
    if len(stack) > 1:
        print(stack.pop(), end=", ")
    else:
        print(stack.pop())