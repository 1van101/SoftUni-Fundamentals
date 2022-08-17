a = int(input())
b = int(input())
max_passwords = int(input())
password_counter = 0
num_1 = 35
num_2 = 64
password_limit_is_reached = False
for num_3 in range(1, a + 1):
    for num_4 in range(1, b + 1):
        password_counter += 1
        print(f"{chr(num_1)}{chr(num_2)}{num_3}{num_4}{chr(num_2)}{chr(num_1)}", end="|")
        if password_counter == max_passwords:
            password_limit_is_reached = True
            break
        num_1 += 1
        num_2 += 1
        if num_1 > 55:
            num_1 = 35
        if num_2 > 96:
            num_2 = 64
    if password_limit_is_reached:
        break







