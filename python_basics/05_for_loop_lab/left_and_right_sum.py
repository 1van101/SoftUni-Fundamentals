num = int(input())

sum_left = 0
sum_right = 0
for i in range (1, num + 1):
    value = int(input())
    sum_left += value

for i in range (1, num + 1):
    value = int(input())
    sum_right += value

difference = abs(sum_left - sum_right)
if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    print(f"No, diff = {difference}")

# num = int(input())
#
# left_sum = 0
# right_sum = 0
#
# for i in range(1, num * 2 + 1):
#     current_num = int(input())
#     if i <= num:
#         left_sum += current_num
#     elif i > num:
#
#         right_sum += current_num
# if left_sum == right_sum:
#     print(f"Yes, sum = {left_sum}")
# else:
#     diff = abs(left_sum - right_sum)
#     print(f"No, diff = {diff}")

