n1 = int(input())
n2 = int(input())

first_start = int(n1 / 1000)
first_end = int(n2 / 1000)
second_start = int((n1 / 100) % 10)
second_end = int((n2 / 100) % 10)
third_start = int((n1 / 10) % 10)
third_end = int((n2 / 10) % 10)
fourth_start = int(n1 % 10)
fourth_end = int(n2 % 10)
for number1 in range(first_start, first_end + 1):
    for number2 in range(second_start, second_end + 1):
        for number3 in range(third_start, third_end + 1):
            for number4 in range(fourth_start, fourth_end + 1):
                if number1 % 2 != 0 and number2 % 2 != 0 and number3 % 2 != 0 and number4 % 2 != 0:
                    print(f'{number1}{number2}{number3}{number4}', end= " " )
# for num1 in range (int(n1[0]), int(n2[0]) + 1)...
