def is_all_valid(*args):
    for num in args:
        if not isinstance(num, int) or num % 2 != 0:
            return False
    return True


def even_parameters(func):
    def wrapper(*args):
        if is_all_valid(*args):
            return func(*args)
        return "Please use only even numbers!"

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
