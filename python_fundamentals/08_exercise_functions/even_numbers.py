def even_numbers(even):
    if even % 2 == 0:
        return True


list_of_numbers = [int(nums) for nums in input().split()]

filtered_list = list(filter(even_numbers, list_of_numbers))

print(filtered_list)

# =============================================================================================
# numbers = input().split()
# nums_as_digits = []
# for number in numbers:
#     nums_as_digits.append((int(number)))
#
# is_even = lambda x: x % 2 == 0
# result = list(filter(is_even, nums_as_digits))
#
# print(result)