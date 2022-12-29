from calculations.operations import all_operations

expression = input().split()
num1 = float(expression[0])
operator = expression[1]
num2 = float(expression[2])

if operator == "/":
    try:
        print(f"{all_operations[operator](num1, num2):.2f}")
    except ZeroDivisionError:
        print("Second num must be not 0")
else:
    print(f"{all_operations[operator](num1, num2):.2f}")