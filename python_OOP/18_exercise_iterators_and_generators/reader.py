def read_next(*args):
    for arg in args:
        i = 0
        while i < len(arg):
            yield list(arg)[i]
            i += 1


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
