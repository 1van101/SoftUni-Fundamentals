num = int(input())

for i in range(1111, 9999 + 1):
    i_str = str(i)

    magic_num_counter = 0
    for position, number in enumerate(i_str):
        if int(number) != 0:
            if num % int(number) == 0:
                magic_num_counter += 1
                if magic_num_counter == 4:
                    print(i_str, end=" ")
                    magic_num_counter = 0

