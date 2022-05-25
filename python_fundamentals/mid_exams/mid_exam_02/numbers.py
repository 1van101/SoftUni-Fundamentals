numbers_input = [int(x) for x in input().split()]

if len(numbers_input) <= 1:
    print("No")
else:
    average_num = sum(numbers_input) // len(numbers_input)
    numbers_input = [x for x in numbers_input if x > average_num]
    if len(numbers_input) < 1:
        print("No")
    else:
        numbers_sorted = sorted(numbers_input, reverse=True)
        if len(numbers_sorted) >= 5:
            for number in range(5):
                print(numbers_sorted[number], end=" ")
        else:
            [print(x, end=" ") for x in numbers_sorted]
