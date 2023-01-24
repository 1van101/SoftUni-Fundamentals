def logged(func):

    def wrapper(*args):
        result = func(*args)
        return f"you called {func.__name__}({', '.join(str(x) for x in args)})\nit returned {result}"

    return wrapper


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

