def sum_numbers(num1, num2):
    return num1 + num2


def subtract(num3, result):
    return result - num3


def add_and_subtract():
    first_num = int(input())
    second_num = int(input())
    third_num = int(input())

    sum = sum_numbers(first_num, second_num)
    sub = subtract(third_num, sum)
    print(sub)


add_and_subtract()
