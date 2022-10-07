def add_numbers(nums_set, *args):
    for num in args:
        nums_set.add(int(num))
    return nums_set


def remove_nums(nums_set, *args):
    return nums_set.difference([int(x) for x in args])


def is_subset(first_nums_set, second_nums_set):
    print(first_nums_set.issubset(second_nums_set) or second_nums_set.issubset(first_nums_set))


first_nums = {int(x) for x in input().split()}
second_nums = {int(x) for x in input().split()}
n = int(input())

for _ in range(n):
    command = input()
    numbers = command.split()[2:]
    if "Add First" in command:
        first_nums = add_numbers(first_nums, *numbers)
    elif "Add Second" in command:
        second_nums = add_numbers(second_nums, *numbers)
    elif "Remove First" in command:
        first_nums = remove_nums(first_nums, *numbers)
    elif "Remove Second" in command:
        second_nums = remove_nums(second_nums, *numbers)
    elif "Check Subset" in command:
        is_subset(first_nums, second_nums)

print(*sorted(first_nums), sep=", ")
print(*sorted(second_nums), sep=", ")
