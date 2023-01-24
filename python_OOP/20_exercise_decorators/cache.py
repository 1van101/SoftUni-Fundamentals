def cache(func):

    def wrapper(num):
        if num not in wrapper.log:
            res = func(num)
            wrapper.log[num] = res

        return wrapper.log[num]


    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
