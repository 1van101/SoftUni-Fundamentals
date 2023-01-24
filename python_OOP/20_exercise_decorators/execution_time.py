import time


def exec_time(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        end = time.time()
        return end - start_time

    return wrapper


@exec_time
def loop():
    count = 0
    for i in range(1, 10_000_000):
        count += 1


print(loop())
