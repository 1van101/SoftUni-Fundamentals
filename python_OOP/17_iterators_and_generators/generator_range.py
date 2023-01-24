def genrange(start, end):
    while start <= end:
        curr_num = start
        start += 1
        yield curr_num


print(list(genrange(1, 10)))