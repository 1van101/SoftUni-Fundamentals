def store_results(func):
    def wrapper(*args):
        res = func(*args)
        func_name = func.__name__
        output = f"Function '{func_name}' was add called. Result: {res}"
        with open("file.txt", "a") as file:
            file.write(output + "\n")


        # return res

    return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
