num1 = int(input())
num2 = int(input())
operator = input()

result = 0
even_or_odd = ""

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{num1} {operator} {num2} = {result} - {even_or_odd}")
elif (operator == "/" or operator == "%") and num2 != 0:
    if operator == "/":
        result = num1 / num2
        print(f"{num1} {operator} {num2} = {result:.2f}")
    elif operator == "%":
        result = num1 % num2
        print(f"{num1} {operator} {num2} = {result}")
else:
    print (f"Cannot divide {num1} by zero")

