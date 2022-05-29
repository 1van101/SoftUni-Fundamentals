def get_sum_even_and_odd(number):
    current_even_sum = 0
    current_odd_sum = 0
    for i in number:
        i = int(i)
        if i % 2 == 0:
            current_even_sum += i
        else:
            current_odd_sum += i
    return current_even_sum, current_odd_sum


number_in_str = input()

even_sum, odd_sum = get_sum_even_and_odd(number_in_str)

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
