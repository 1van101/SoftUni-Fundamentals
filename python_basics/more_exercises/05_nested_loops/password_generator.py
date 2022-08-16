n = int(input())
l = int(input())
for first_num in range(1, n):
    for second_num in range(1, n):
        for third_num in range(97, l + 97):
            for fourth_num in range(97, l + 97):
                for fifth_num in range(1, n + 1):
                    if fifth_num > first_num and fifth_num > second_num:
                        print(f"{first_num}{second_num}{chr(third_num)}{chr(fourth_num)}{fifth_num}", end=" ")