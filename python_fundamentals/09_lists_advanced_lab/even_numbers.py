numbers = [int(x) for x in input().split(", ")]
result = [(x[0]) for x in enumerate(numbers) if x[1] % 2 == 0]
print(result)

#======================================
# str_with_nums = input().split(", ")

# list_with_indexes = []

# for i, n in enumerate(str_with_nums):
#     n = int(n)
#     if n % 2 == 0:
#         list_with_indexes.append(i)
# print(list_with_indexes)