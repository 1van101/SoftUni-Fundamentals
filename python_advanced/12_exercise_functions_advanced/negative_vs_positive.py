nums = [int(x) for x in input().split()]
negatives = sum([x for x in nums if x < 0])
positives = sum([x for x in nums if x > 0])

print(f"{negatives}\n{positives}")

if positives > abs(negatives):
    print(f"The positives are stronger than the negatives")
else:
    print(f"The negatives are stronger than the positives")
# ================================================================
# def sum_of_numbers(nums):
#     sum_of_positives = 0
#     sum_of_negatives = 0
#     for num in nums:
#         if num >= 0:
#             sum_of_positives += num
#         else:
#             sum_of_negatives += num
#     return sum_of_positives, sum_of_negatives
#
#
# numbers = [int(x) for x in input().split()]
# positives, negatives = sum_of_numbers(numbers)
#
# print(f"{negatives}\n{positives}")
# if positives > abs(negatives):
#     print(f"The positives are stronger than the negatives")
# elif positives < abs(negatives):
#     print(f"The negatives are stronger than the positives")