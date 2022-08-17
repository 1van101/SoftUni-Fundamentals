first_pair_min = int(input())
second_pair_min = int(input())
first_pair_diff = int(input())
second_pair_diff = int(input())
first_pair_max = first_pair_min + first_pair_diff
second_pair_max = second_pair_diff + second_pair_min

for first_pair in range(first_pair_min, first_pair_max + 1):
    flag_first_pair = False
    for i in range(2, first_pair):
        if first_pair % i == 0:
            flag_first_pair = True
            break

    if flag_first_pair:
        pass
    else:
        for second_pair in range(second_pair_min, second_pair_max + 1):
            flag_second_pair = False
            for j in range(2, second_pair):
                if second_pair % j == 0:
                    flag_second_pair = True
                    break

            if flag_second_pair:
                pass
            else:
                print(f"{first_pair}{second_pair}")






