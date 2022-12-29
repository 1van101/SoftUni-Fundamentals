def print_triangle(n, i=1):
    if i == n + 1:
        return
    print(*[x for x in range(1, i + 1)])
    print_triangle(n, i+1)
    print(*[x for x in range(1, i)])