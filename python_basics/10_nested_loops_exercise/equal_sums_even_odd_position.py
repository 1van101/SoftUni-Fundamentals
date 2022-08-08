num_1 = int(input())
num_2 = int(input())

for number in range (num_1, num_2 + 1):
    sum_even = 0
    sum_odd = 0
    number_to_str = str(number)
    for index, symbol in enumerate(number_to_str):
        if int(index) % 2 == 0:
            sum_even += int(symbol)
        else:
            sum_odd += int(symbol)

    if sum_even == sum_odd:
        print(number, end=" ")

