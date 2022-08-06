first_num = int(input())
last_num = int(input())
magic_num = int(input())

counter = 0
current_x1 = ""
current_x2 = ""
is_valid = False
for x1 in range(first_num, last_num + 1):
    for x2 in range(first_num, last_num + 1):
        counter += 1
        if x1 + x2 == magic_num:
            current_x1 = x1
            current_x2 = x2
            is_valid = True
            break
    if is_valid:
        break
if is_valid:
    print(f"Combination N:{counter} ({current_x1} + {current_x2} = {magic_num})")
else:
    print(f"{counter} combinations - neither equals {magic_num}")