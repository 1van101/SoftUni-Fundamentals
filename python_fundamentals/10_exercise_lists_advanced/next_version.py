def print_new_version(numbers):
    numbers[-1] += 1
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] > 9:
            numbers[i] = 0
            if i - 1 >= 0:
                numbers[i - 1] += 1
    print(".".join(str(x) for x in numbers))


version_in_int = [int(x) for x in input().split(".")]
print_new_version(version_in_int)
