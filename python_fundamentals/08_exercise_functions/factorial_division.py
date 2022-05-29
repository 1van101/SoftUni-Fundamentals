def get_factorial(number):
    for factorial in range(1, number):
        number *= factorial
    return number


def get_division(num1, num2):
    first_num_factorial = get_factorial(num1)
    second_num_factorial = get_factorial(num2)
    return first_num_factorial / second_num_factorial


first_num = int(input())
second_num = int(input())

division = get_division(first_num, second_num)
print(f"{division:.2f}")