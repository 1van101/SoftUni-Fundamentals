number_of_men = int(input())
number_of_women = int(input())
max_number_tables = int(input())
counter = 0
for i in range(1, number_of_men + 1):
    for j in range(1, number_of_women + 1):

        if counter == max_number_tables:
            break
        counter += 1
        print(f"({i} <-> {j})", end=" ")