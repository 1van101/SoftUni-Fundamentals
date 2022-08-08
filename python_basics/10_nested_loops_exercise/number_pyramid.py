n = int(input())

current_n = 1
is_current_n_bigger = False

for row in range(1, n + 1):
    for column in range(1, row + 1):
        if current_n > n:
            is_current_n_bigger = True
            break
        print (f"{current_n} ", end="")

        current_n += 1
    if is_current_n_bigger:
        break
    print()
# num = int(input())
# counter = 1
# for r in range(1, num + 1):
#     for c in range(1, r + 1):
#         if counter > num:
#             break
#         print(counter, end=" ")
#         counter += 1
#     if counter > num:
#         break
#     print()

# num = int(input())
# counter = 1
# valid = False
# for i in range(1, num + 1):
#     for j in range(1, i + 1):
#         print(counter, end=" ")
#         counter += 1
#         if counter > num:
#             valid = True
#             break
#     if valid:
#         break
#     print()


