list_of_numbers = [int(x) for x in input().split(", ")]
number_of_beggars = int(input())

final_list = []

for beggar in range(number_of_beggars):
    current_list = []
    for current_beggar in range(beggar, len(list_of_numbers), number_of_beggars):
        current_list.append(list_of_numbers[current_beggar])
    final_list.append(sum(current_list))

print(final_list)
