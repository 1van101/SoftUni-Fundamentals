min_num = int(input())
max_num = int(input())
magic_num = int(input())
counter = 0
combination_is_found = False

for num_1 in range(min_num, max_num + 1):
    for num_2 in range(min_num, max_num + 1):
        counter += 1
        if num_1 + num_2 == magic_num:
            print(f"Combination N:{counter} ({num_1} + {num_2} = {magic_num})")
            combination_is_found = True
            break
    if combination_is_found:
        break
if not combination_is_found:
    print(f"{counter} combinations - neither equals {magic_num}")