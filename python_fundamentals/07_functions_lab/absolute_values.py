def get_abs_value(numbers):
    return [abs(x) for x in numbers]


numbers_list = [float(x) for x in input().split()]

print(get_abs_value(numbers_list))