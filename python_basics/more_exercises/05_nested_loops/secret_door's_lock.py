n1_max = int(input())
n2_max = int(input())
n3_max = int(input())
for num_1 in range(2, n1_max + 1, 2):
    for num_2 in range(2, n2_max + 1):
        for num_3 in range(2, n3_max + 1, 2):
            if num_2 == 2 or num_2 == 3 or num_2 == 5 or num_2 == 7:
                print(f"{num_1} {num_2} {num_3}")