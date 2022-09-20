from collections import deque

children = deque(input().split())
n = int(input())

while children:
    children.rotate(-n + 1)
    print(f"Removed {children.popleft()}") if len(children) > 1 else print(f"Last is {children.popleft()}")
