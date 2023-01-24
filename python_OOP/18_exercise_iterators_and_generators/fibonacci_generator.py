def fibonacci():
    first = 0
    second = 1

    yield first
    yield second

    while True:
        next_num = first + second
        yield next_num
        first = second
        second = next_num


generator = fibonacci()
for i in range(5):
    print(next(generator))

