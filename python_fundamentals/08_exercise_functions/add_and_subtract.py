def sum_numbers(num1, num2):
    return num1 + num2


def subtract(num3, result):
    return result - num3


def add_and_subtract(num1, num2, num3):
    sum = sum_numbers(num1, num2)
    sub = subtract(num3, sum)
    return sub

first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))
