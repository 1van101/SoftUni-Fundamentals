def squares(n):
    num = 0
    while num < n:
        num += 1
        yield num * num


print(list(squares(5)))