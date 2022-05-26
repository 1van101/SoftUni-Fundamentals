def get_result(num1, num2, num3):
    number_of_negatives = 0
    list_of_nums = [num1, num2, num3]

    for x in list_of_nums:
        if x < 0:
            number_of_negatives += 1
        elif x == 0:
            return "zero"
    if number_of_negatives % 2 != 0:
        return "negative"
    else:
        return "positive"

first_number = int(input())
second_number = int(input())
third_number = int(input())
print(get_result(first_number, second_number, third_number))

