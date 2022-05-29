employees_happiness = [int(x) for x in input().split()]
happiness_factor = int(input())

multiplied_list = list(map(lambda x: x * happiness_factor, employees_happiness))
average_res = sum(multiplied_list) / len(multiplied_list)

filtered_list = [x for x in multiplied_list if x > average_res]  # -> filtered_list = list(filter(lambda x: x >= average_res, multiplied_list))

if len(filtered_list) >= len(multiplied_list) / 2:
    print(f"Score: {len(filtered_list)}/{len(multiplied_list)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_list)}/{len(multiplied_list)}. Employees are not happy!")