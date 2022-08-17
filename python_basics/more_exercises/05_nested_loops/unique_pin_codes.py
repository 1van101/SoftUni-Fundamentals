num_1_end = int(input())
num_2_end = int(input())
num_3_end = int(input())

for num1 in range(2, num_1_end + 1, 2):
    for num2 in range(2, num_2_end + 1):
        for num3 in range(2, num_3_end + 1, 2):
            if num2 in (2, 3, 5, 7):
                print(f"{num1} {num2} {num3}")

# num_1_end = int(input())
# num_2_end = int(input())
# num_3_end = int(input())
#
# for num1 in range(2, num_1_end + 1, 2):
#     for num2 in range(2, num_2_end + 1):
#         valid = False
#         for num_prime in range(2, num2):
#             if num2 % num_prime == 0:
#                 valid = True
#                 break
#         if valid:
#             pass
#         else:
#             for num3 in range(2, num_3_end + 1, 2):
#                 print(f"{num1} {num2} {num3}")

