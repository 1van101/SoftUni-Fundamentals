command = input()
sum_prime_numbers = 0
sum_non_prime_numbers = 0
while command != "stop":
    current_num = int(command)
    if current_num < 0:
        print("Number is negative.")
    else:
        non_prime = False
        for num in range(2, current_num):
            if current_num % num == 0:
                    non_prime = True
                    break
        if non_prime:
            sum_non_prime_numbers += current_num
        else:
            sum_prime_numbers += current_num

    command = input()

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")

# prime_numbers_sum = 0
# non_prime_numbers_sum = 0
# while True:
#     is_non_prime = False
#     command = input()
#     if command == "stop":
#         break
#     command_int = int(command)
#     if command_int < 0:
#         print("Number is negative.")
#         continue
#     elif command_int == 1:
#         continue
#     else:
#         for num in range(2, command_int):
#             if command_int % num == 0:
#                 is_non_prime = True
#                 break
#         if is_non_prime:
#             non_prime_numbers_sum += command_int
#         else:
#             prime_numbers_sum += command_int
# print(f"Sum of all prime numbers is: {prime_numbers_sum}")
# print(f'Sum of all non prime numbers is: {non_prime_numbers_sum}')


