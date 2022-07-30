type_projection = input()
number_of_rows = int(input())
number_of_columns = int(input())

price = 0

if type_projection == "Premiere":
    price = 12.00
elif type_projection == "Normal":
    price = 7.50
elif type_projection == "Discount":
    price = 5.00

total_income = number_of_rows * number_of_columns * price

print(f"{total_income:.2f} leva")