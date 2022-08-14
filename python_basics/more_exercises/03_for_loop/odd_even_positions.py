import sys

num = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

num_is_less_than_1 = False
num_is_less_than_2 = False

if num < 1:
    odd_max = odd_min = even_max = even_min = "No"
    num_is_less_than_1 = True
elif num < 2:
    even_min = even_max = "No"
    num_is_less_than_2 = True

for i in range(1, num + 1):
    current_num = float(input())
    if i % 2 == 0:
        if i == 2:
            even_min = current_num
            even_max = current_num

        even_sum += current_num
        if current_num > even_max:
            even_max = current_num
        elif current_num < even_min:
            even_min = current_num
    else:
        if i == 1:
            odd_min = current_num
            odd_max = current_num

        odd_sum += current_num
        if current_num > odd_max:
            odd_max = current_num
        elif current_num < odd_min:
            odd_min = current_num

if num_is_less_than_2:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min},")
    print(f"EvenMax={even_max}")
elif num_is_less_than_1:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min},")
    print(f"OddMax={odd_max},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min},")
    print(f"EvenMax={even_max}")
else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")


