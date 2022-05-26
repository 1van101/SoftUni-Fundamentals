def calculations(operator, num1, num2):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return num1 // num2
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2


operator_str = input()
first_num = int(input())
second_num = int(input())

print(calculations(operator_str, first_num, second_num))
