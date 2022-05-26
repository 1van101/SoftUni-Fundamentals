def unpacked_list(list_of_nums):
    return ", ".join(str(x) for x in list_of_nums)


numbers_list = input().split(", ")
numbers_list = [int(x) for x in numbers_list]

positive_nums = [x for x in numbers_list if x >= 0]
negative_nums = [x for x in numbers_list if x < 0]
even_nums = [x for x in numbers_list if x % 2 == 0]
odd_nums = [x for x in numbers_list if not x % 2 == 0]

print(f"Positive: {unpacked_list(positive_nums)}")
print(f"Negative: {unpacked_list(negative_nums)}")
print(f"Even: {unpacked_list(even_nums)}")
print(f"Odd: {unpacked_list(odd_nums)}")