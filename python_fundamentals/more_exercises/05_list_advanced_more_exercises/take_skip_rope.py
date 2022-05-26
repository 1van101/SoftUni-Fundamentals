import re

hidden_message = input()
numbers = []
non_numbers = []
take_list = []
skip_list = []
taken_string = ""
skipped_string = ""

for char in hidden_message:
    if char.isdigit():
        numbers.append(char)
    else:
        non_numbers.append(char)

for index in range(len(numbers)):
    if index % 2 == 0:
        take_list.append(numbers[index])
    else:
        skip_list.append(numbers[index])


for i in range(len(numbers) // 2):
    current_number_to_take = int(take_list[i])
    if current_number_to_take != 0:
        for take in range(current_number_to_take):
            if len(non_numbers) == 0:
                break
            taken_string += non_numbers[0]
            non_numbers.pop(0)
    current_number_to_skip = int(skip_list[i])
    if current_number_to_skip != 0:
        for skip in range(current_number_to_skip):
            if len(non_numbers) == 0:
                break
            skipped_string += non_numbers[0]
            non_numbers.pop(0)

print(taken_string)


