def swap_places(numbers, first, second):
    numbers[first], numbers[second] = numbers[second], numbers[first]
    return numbers


def multiply_numbers(numbers, first, second):
    numbers[first] = numbers[first] * numbers[second]
    return numbers


def decrease_elements(numbers):
    for i in range(len(numbers)):
        numbers[i] -= 1
    return numbers


numbers_input = [int(x) for x in input().split()]

while True:
    command = input().split()
    if command[0] == "end":
        break

    if "decrease" in command:
        decrease_elements(numbers_input)     #[x - 1 for x in numbers_input]
    elif "swap" in command:
        swap_places(numbers_input, int(command[1]), int(command[2]))
    elif "multiply" in command:
        multiply_numbers(numbers_input, int(command[1]), int(command[2]))

numbers_input = [str(x) for x in numbers_input]
print(", ".join(numbers_input))
